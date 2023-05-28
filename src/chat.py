# Get Imports 
import os
from pathlib import Path
from llama_index import download_loader, GPTVectorStoreIndex
from langchain import OpenAI

# Get API KEYS
os.environ['OPENAI_API_KEY'] = str(os.getenv("OPENAI_APIKEY"))

# Define Data For Chat Bot
pdfreader = download_loader("PDFReader")

# Load Data
loader = pdfreader()
documents = loader.load_data(file=Path('src/Martin.pdf'))

# Vector Indexing 
pdf_index = GPTVectorStoreIndex.from_documents(documents)
query_engine = pdf_index.as_query_engine()

bot_name = "Monday"

# Run Chat
def get_response(msg):
    msg = str(msg)
    #print("Let's chat! (type 'quit' or 'bye' to exit)")
    if msg.lower() in ["quit", "bye", "goodbye", "stop"]:
        resp = "Have a great day!"
    else:
        resp = query_engine.query(msg) 
    
    return str(resp) 