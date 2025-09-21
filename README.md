# Recipe Suggestions RAG

## Environment Variables
> GOOGLE_API_KEY

To run this project, you will need to add the following environment variables to your .evn file

## Usage

Clone the repository
```
git clone https://github.com/Pedro1697/Recipe-Suggestions-RAG.git
```
Go to the project directory
```
cd Recipe-Suggestions-RAG
```
Install dependecies 
```
poetry install
```

Run the project
```
python main " ingredients" 
```
Ex: ingredeints: "pasta, salami, tomato"

## Project Structure

* database 
* utils
* poetry.lock
* pyproject.toml
* main.py

## Technologies Used

### Languages
- **Python** 

### Frameworks and Libraries
- **LangChain** – RAG and prompt chain management.
- **ChromaDB** – Vector database for storing and searching embeddings.
- **HuggingFace Embeddings** (`all-MiniLM-L6-v2`) – Text vector generation.
- **Pandas** – Data loading and manipulation.
- **RecursiveCharacterTextSplitter** – Splitting text into manageable chunks.

### Tools
- **Poetry / pip** – Dependency management.
- **VSCode** – Main IDE.
- **.env** – Environment variables (API keys, paths, etc.).
- **Git** – Version control.


