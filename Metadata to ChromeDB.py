import chromadb
import json
from openai import OpenAI  # New import for OpenAI v1.0+

client = OpenAI(api_key="Your API key here.")  # Use your OpenAI API key

# Load metadata
with open("floor_plan_metadata.json", "r") as file:
    floor_plans = json.load(file)

# Initialize ChromaDB
chroma_client = chromadb.PersistentClient(path="chroma_db")
collection = chroma_client.get_or_create_collection(name="floor_plans")

# OpenAI Embedding Function
def get_embedding(text):
    response = client.embeddings.create(
        model="text-embedding-ada-002",
        input=text
    )
    return response.data[0].embedding

# Insert each floor plan into ChromaDB
for idx, plan in enumerate(floor_plans):
    metadata_text = f"Rooms: {plan['extracted_text']}, Area: {plan.get('estimated_sqft', 'unknown')} sqft"
    embedding = get_embedding(metadata_text)

    collection.add(
        ids=[str(idx)],  # Required unique ID for each entry
        embeddings=[embedding],
        documents=[metadata_text],
        metadatas=[{"file_path": plan["file_path"], "sqft": plan.get("estimated_sqft", "unknown")}]
    )

print("Floor plans inserted into ChromaDB")
