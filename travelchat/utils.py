import os
import dotenv
from openai import OpenAI
from hooks import qdrant_hook

dotenv.load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")

openai_client = OpenAI(api_key=openai_api_key)


def embed_text(text):
    embeddings = openai_client.embeddings.create(input=text, model="text-embedding-ada-002").data[0].embedding
    return embeddings


def query(text, top_k=3):
    vector = embed_text(text)
    results = [
                {
                    "id": match.id,
                    "score": match.score,
                    "payload": match.payload,
                }
                for match in qdrant_hook.query_document(vector, top_k)
            ]
    
    return results