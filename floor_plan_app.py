import streamlit as st
import chromadb
from openai import OpenAI
from PIL import Image
import os

# Load OpenAI API key securely
OPENAI_API_KEY = "Your API key here."  # User inputs API key


if OPENAI_API_KEY:
    client = OpenAI(api_key=OPENAI_API_KEY)  # Initialize OpenAI client

    # Initialize ChromaDB client
    chroma_client = chromadb.PersistentClient(path="chroma_db")
    collection = chroma_client.get_or_create_collection(name="floor_plans")

    def generate_embedding(text):
        response = client.embeddings.create(
            model="text-embedding-ada-002",
            input=[text]
        )
        return response.data[0].embedding

    def search_floor_plans(query, top_k=5):
        query_embedding = generate_embedding(query)
        results = collection.query(
            query_embeddings=[query_embedding],
            n_results=top_k
        )
        return results

    # Streamlit UI
    st.title("🏠 Floor Plan Generator")
    st.write("Generate architectural floor plans using natural language.")

    search_query = st.text_input("🔍 Enter search query (e.g., '2BHK with balcony, 1000 sqft')")

    if st.button("Generate"):
        if search_query:
            st.write("🤖 Generating... Please wait.")
            search_results = search_floor_plans(search_query)

            if search_results and "documents" in search_results:
                for idx, doc in enumerate(search_results["documents"][0]):  # Loop through results
                    if os.path.exists(doc):
                        st.write(f"**Result {idx+1}:**")
                        st.image(doc, caption=f"Floor Plan {idx+1}", use_container_width=True)  # Fixes deprecated warning
                        st.write("---")
                    else:
                        st.write(f"❌ Could'nt generate image, try Rephrasing your Prompt")  #st.write(f"❌ Image not found: {doc}")
            else:
                st.write(f"❌ Could'nt generate image, try Rephrasing your Prompt")  #st.write("No matching floor plans found.")
        else:
            st.write("⚠️ Please enter a search query.")

# Run using:
# streamlit run floor_plan_app.py Or python -m streamlit run floor_plan_app.py

