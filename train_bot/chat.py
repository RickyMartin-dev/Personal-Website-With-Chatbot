import os
from llama_index import download_loader, LLMPredictor, GPTSimpleVectorIndex, PromptHelper, ServiceContext
from langchain import OpenAI

#print(os.environ.get('WHO_TO_TRUST'), os.environ['WHO_TO_TRUST'])
temp = str(os.getenv("OPENAI_APIKEY"))
print(temp)
print()
os.environ['OPENAI_API_KEY'] = temp

DadJokesReader = download_loader("DadJokesReader")

loader = DadJokesReader()
documents = loader.load_data()

dad_index = GPTSimpleVectorIndex.from_documents(documents)

bot_name = "Monday"

def get_response(msg):
    msg = str(msg)
    #print("Let's chat! (type 'quit' or 'bye' to exit)")
    if msg.lower() in ["quit", "bye", "goodbye", "stop"]:
        resp = "Have a great day!"
    else:
        resp = dad_index.query(msg)
    
    return str(resp)