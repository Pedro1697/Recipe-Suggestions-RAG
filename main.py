import argparse
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_google_genai import GoogleGenerativeAI
from langchain_chroma import Chroma
from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate

load_dotenv()

CHROMA_PATH = "chroma_db/"


PROMPT_TEMPLATE = """
You are a food adviser. You have to give the name and steps to prepare the meal

your job is to give the answer to the strictly answer user query
The user will give you the {ingredients} that they have.

 With the ingredients you have to give them a
suggestion using the {context} about a dish they can do with the ingredients or the most similar dish with the ingredients 

"""

def recipe_suggestion():
    #print("Give me the ingredients that you have: ")
    parser = argparse.ArgumentParser()
    parser.add_argument("ingredients",type=str,help="List of ingredients provided by the user")
    args = parser.parse_args()
    ingredients = args.ingredients

    #Prepare the database 
    embedding_function = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    db = Chroma(persist_directory=CHROMA_PATH,embedding_function=embedding_function)

    # Search the database
    results = db.similarity_search_with_relevance_scores(ingredients,k=2)
    if len(results)==0 or results[0][1] < 0.2:
        print("I have not any recommendation")
        return
    
    context_text = "\n\n---\n\n".join([doc.page_content for doc, _score in results])
    prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
    prompt = prompt_template.format(context=context_text,ingredients=ingredients)
    print(prompt)

    model = GoogleGenerativeAI(model="gemini-2.5-flash")
    response_text = model.invoke(prompt)

    

if __name__ == "__main__":
    #print("First project using RAG")
    recipe_suggestion()