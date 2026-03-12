import yaml
import requests
from qdrant_client import QdrantClient


OLLAMA_URL = "http://ollama:11434/api/generate"
EMBED_URL = "http://ollama:11434/api/embeddings"


def load_config():
    with open("config.yaml") as f:
        return yaml.safe_load(f)


config = load_config()

client = QdrantClient(
    host=config["qdrant"]["host"],
    port=config["qdrant"]["port"]
)


def embed_query(query):

    response = requests.post(
        EMBED_URL,
        json={
            "model": config["ollama"]["embedding_model"],
            "prompt": query
        }
    )

    data = response.json()

    if "embedding" not in data:
        raise Exception(f"Ollama embedding error: {data}")

    return data["embedding"]


def ask_llm(context, question):

    prompt = f"""
You are an HR assistant.

Use the provided context to answer the question.

Context:
{context}

Question:
{question}

Please answer only from the document.
Be clear and concise.
"""

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": config["ollama"]["llm_model"],
            "prompt": prompt,
            "stream": False
        }
    )

    data = response.json()

    if "response" not in data:
        raise Exception(f"Ollama generation error: {data}")

    return data["response"]


def ask_question(question):

    query_vector = embed_query(question)

    results = client.query_points(
        collection_name=config["qdrant"]["collection_name"],
        query=query_vector,
        limit=3
    )

    context = "\n".join(
        point.payload["text"] for point in results.points
    )

    answer = ask_llm(context, question)

    return answer