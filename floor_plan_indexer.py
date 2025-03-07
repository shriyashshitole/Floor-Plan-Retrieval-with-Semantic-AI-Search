import os
import chromadb
from openai import OpenAI
import json

# Secure API key input
OPENAI_API_KEY = "Your API key here."
client = OpenAI(api_key=OPENAI_API_KEY)  # Initialize OpenAI client

# Initialize ChromaDB client
chroma_client = chromadb.PersistentClient(path="chroma_db")
collection = chroma_client.get_or_create_collection(name="floor_plans")

# Function to generate embeddings using OpenAI API
def generate_embedding(text):
    response = client.embeddings.create(
        model="text-embedding-ada-002",
        input=text  # Ensure it's a string, not a list
    )
    return response.data[0].embedding

# Function to index a floor plan
def index_floor_plan(description, image_path):
    if not os.path.exists(image_path):
        print(f"Skipping: File not found -> {image_path}")
        return
    
    embedding = generate_embedding(description)
    collection.add(
        ids=[image_path],
        documents=[image_path],
        embeddings=[embedding],
        metadatas=[{"description": description}]
    )
    print(f"Indexed: {image_path}")

# Index all floor plans from metadata file
metadata_file = "floor_plan_metadata.json"

if os.path.exists(metadata_file):
    with open(metadata_file, "r") as file:
        floor_plans = json.load(file)

    for plan in floor_plans:
        index_floor_plan(description=plan["extracted_text"], image_path=plan["file_path"])
    print("Floor plans indexed successfully.")
else:
    print(f"Metadata file not found: {metadata_file}")
