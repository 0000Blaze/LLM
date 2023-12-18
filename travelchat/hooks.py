from qdrant_client import QdrantClient, models
from qdrant_client.http.models import PointStruct
import dotenv
import os

dotenv.load_dotenv()

qdrant_host = os.getenv("QDRANT_HOST")
qdrant_api_key = os.getenv("QDRANT_API_KEY")


class QdrantHook:
    def __init__(self, collection_name: str) -> None:
        self.client = QdrantClient(
            url=qdrant_host,
            api_key=qdrant_api_key,
        )
        self.collection_name = collection_name
        if not self.check_collection_exists():
            self.create_collection()

    def check_collection_exists(self) -> bool:
        return any(collection.name == self.collection_name for collection in self.client.get_collections().collections)

    def create_collection(self) -> bool:
        return self.client.create_collection(
            collection_name=self.collection_name,
            vectors_config=models.VectorParams(
                size=1536,
                distance=models.Distance.COSINE,
            ),
        )

    def upsert_document(self, documents: list) -> bool | None:
        try:
            for i in range(0, len(documents), 10):
                self.client.upsert(
                    collection_name=self.collection_name,
                    wait=True,
                    points=[
                        PointStruct(id=doc["id"], vector=doc["embedding"], payload=doc["metadata"])
                        for doc in documents[i : i + 10]
                    ],
                )

            return True
        except Exception as e:
            print(f"An error occurred while upserting documents: {str(e)}")
            return None

    def query_document(self, vector: list[float], top_k: int = 4) -> list[dict]:
        return self.client.search(
            collection_name=self.collection_name,
            query_vector=vector,
            limit=top_k,
        )


qdrant_hook = QdrantHook("travelchat")
