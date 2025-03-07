# 🏠 Floor Plan Retrieval with OpenAI & ChromaDB

This project enables **semantic search** for architectural **floor plans** using **OpenAI embeddings** and **ChromaDB**. Users can search for floor plans using natural language queries, and the most relevant images are retrieved and displayed.

## 📌 Features
- ✅ **Store & Search Floor Plans** – Uses OpenAI embeddings to store and retrieve images.  
- ✅ **ChromaDB for Vector Search** – Efficient similarity-based search.  
- ✅ **Streamlit Web Interface** – Simple & interactive UI.  
- ✅ **Automatic Metadata Extraction** – Stores floor plans with descriptions & square footage.  

## 📂 Project Structure

📁 project_root/ 
│── 📂 floor_plans/ # Folder containing floor plan images 
│── 📄 floor_plan_metadata.json # Metadata with descriptions & paths 
│── 📜 floor_plan_indexer.py # Indexes floor plans into ChromaDB 
│── 📜 floor_plan_app.py # Streamlit app for searching floor plans 
│── 📂 chroma_db/ # ChromaDB database storage 
│── 📄 README.md # This file!


## 🔧 Installation

1️⃣ Clone the Repository
bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name

2️⃣ Install Dependencies
Ensure you have Python 3.8+ installed.

pip install -r requirements.txt

3️⃣ Set Up OpenAI API Key:
Get your OpenAI API key from OpenAI Dashboard.
Store it securely (do not hardcode it).
You can set it dynamically when running the app.

🚀 Usage
1️⃣ Index Floor Plans
Run the indexer to store embeddings in ChromaDB:

bash:
python floor_plan_indexer.py

2️⃣ Run the Web App
Launch the Streamlit app:

bash:
streamlit run floor_plan_app.py

3️⃣ Search for Floor Plans
Enter a natural language query (e.g., "2BHK apartment with 1000 sqft").
The system retrieves and displays similar floor plan images.

🛠 Troubleshooting
1️⃣ Image Not Found?
Make sure the floor_plans/ folder contains images.
Check file paths in floor_plan_metadata.json:
json:
{"file_path": "floor_plans/0_1.jpg"}

Run:
bash:
python -c "import os; print(os.listdir('floor_plans'))"

2️⃣ OpenAI API Errors?
Ensure the API key is correct.
Upgrade OpenAI package:
bash:
pip install --upgrade openai

3️⃣ ChromaDB Not Searching?
Run:
bash:
python -c "import chromadb; db = chromadb.PersistentClient(path='chroma_db'); print(db.get_collection('floor_plans').get())"
If empty, re-run floor_plan_indexer.py.

🤝 Contributing
Feel free to submit issues or pull requests! 🚀

📜 License
This project is licensed under the MIT License.
