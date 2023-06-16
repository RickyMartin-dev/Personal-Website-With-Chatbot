# Get Imports 
import os
from langchain.llms import OpenAI
from langchain.vectorstores import FAISS
from langchain.prompts import PromptTemplate
from langchain.document_loaders import TextLoader
from langchain.memory import ConversationBufferMemory
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.chains.question_answering import load_qa_chain

# Get API KEYS
os.environ['OPENAI_API_KEY'] = str(os.getenv("OPENAI_APIKEY"))

# Load resume text information
loader = TextLoader("src/Martin_Resume.txt")

# Load document
docs = loader.load()

# Text embedder for document
text_splitter = CharacterTextSplitter(separator = "\n",chunk_size = 300,chunk_overlap  = 200,length_function = len)

# text embedding
docs = text_splitter.split_documents(docs)
docsearch = FAISS.from_documents(docs, OpenAIEmbeddings())

# Chat Template
template = """You are a chatbot having a conversation with a human, respond in a comical way and make sure your output is less than 50 words long.
Given the following extracted context and a question, create a final answer.
{context}
{chat_history}
Human: {human_input}
Chatbot:"""

# Chat Prompt
prompt = PromptTemplate(input_variables=["chat_history", "human_input", "context"],template=template)

# Chat Memory
memory = ConversationBufferMemory(memory_key="chat_history", input_key="human_input")

# Chat QA chain
chain = load_qa_chain(OpenAI(temperature=0.7), chain_type="stuff", memory=memory, prompt=prompt)

# Run the chat bot
def get_response(msg):

    msg = str(msg)

    if msg.lower() in ["quit", "bye", "goodbye", "stop"]:
        resp = "Have a great day!"
    else:
        docs = docsearch.similarity_search(msg)
        values = chain({"input_documents": docs, "human_input": msg}, return_only_outputs=True)
        resp = str(values['output_text'])
    return str(resp) 