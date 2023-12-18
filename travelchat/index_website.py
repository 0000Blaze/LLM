import dotenv
import os
import uuid
import json
from langchain.text_splitter import RecursiveCharacterTextSplitter
from openai import OpenAI
from hooks import qdrant_hook

dotenv.load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")

openai_client = OpenAI(api_key=openai_api_key)

def create_composite_key(url, section_index, chunk_index):
    url_with_parameters = f"{url}{section_index}{chunk_index}"
    url_uuid = str(uuid.uuid5(uuid.NAMESPACE_URL, url_with_parameters))

    return url_uuid

def load_json_files(directory_path):
    all_lists = []

    for filename in os.listdir(directory_path):
        if filename.endswith(".json"):
            file_path = os.path.join(directory_path, filename)

            with open(file_path, 'r') as file:
                json_list = json.load(file)

            all_lists.extend(json_list)

    return all_lists


def process_news_data_in_vector(article):
    print(f"Indexing article: {article.get('url')}")
    content = article.get("content", [])
    splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
        chunk_size=250,
        chunk_overlap=10,
        separators=["\n\n", "\n", " ", ""],
    )

    chunks = [
        {
            "id": create_composite_key(article.get("url"), section_index, chunk_index),
            "text": (
                f'#{article.get("title")}\n\n'
                + (f"##{section.get('section_header')}\n" if section.get("section_header") else "")
                + chunk
            ),
            "metadata": {
                "title": article.get("title"),
                "url": article.get("url"),
                "chunk_index": chunk_index,
                "section_index": section_index,
            },
            "chunk_index": chunk_index,
            "section_index": section_index,
        }
        for section_index, section in enumerate(content)
        for chunk_index, chunk in enumerate(splitter.split_text("\n".join(section["section_content"])))
        if len("\n".join(section["section_content"])) >= 50
    ]

    embs = openai_client.embeddings.create(
        input=[chunk["text"] for chunk in chunks], model="text-embedding-ada-002"
    ).data

    documents = [
        {"id": chunk["id"], "embedding": e.embedding, "metadata": {**chunk["metadata"], "content": chunk["text"]}}
        for chunk, e in zip(chunks, embs)
    ]

    if not qdrant_hook.upsert_document(documents):
        return None

    return [{key: value for key, value in chunk.items() if key != "metadata"} for chunk in chunks]

directory_path = './website_json'
resulting_list = load_json_files(directory_path)

for article in resulting_list:
    print("Processing article: ", article.get("url"))
    try:
        process_news_data_in_vector(article)
    except Exception as e:
        print(f"An error occurred while processing article: {str(e)}")
        continue
