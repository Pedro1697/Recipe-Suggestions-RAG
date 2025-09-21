import sys
import os 
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain.schema import Document
from dotenv import load_dotenv
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.helpers import read_csv_in_chunks


# Name, RecipeInghredientsParts,RecipeInstructions

load_dotenv()
os.makedirs("chroma_db",exist_ok=True)

embedding_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
splitter = RecursiveCharacterTextSplitter(chunk_size=1000,chunk_overlap=200)

vector_store = Chroma(persist_directory="chroma_db",embedding_function=embedding_model)

for chunk in read_csv_in_chunks("data/recipes_20k.csv",chunk_size=500):
    texts = ["{}: {} - {}".format(r["Name"], r["RecipeIngredientParts"], r["RecipeInstructions"]) for r in chunk]
    docs = [Document(page_content=t) for t in texts]
    all_splits = splitter.split_documents(docs)
    vector_store.add_documents(all_splits)  
