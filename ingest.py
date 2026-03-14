import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.embeddings import SentenceTransformerEmbeddings
from langchain_community.vectorstores import Chroma

all_docs = []

# Load all PDFs
for root, dirs, files in os.walk("data"):
    for file in files:
        if file.endswith(".pdf"):
            path = os.path.join(root, file)

            print(f"Loading {path}")

            loader = PyPDFLoader(path)
            documents = loader.load()

            all_docs.extend(documents)

# Split text
text_splitter = CharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

docs = text_splitter.split_documents(all_docs)

# Create embeddings
embedding_model = SentenceTransformerEmbeddings(
    model_name="all-MiniLM-L6-v2"
)

# Store in ChromaDB
db = Chroma.from_documents(
    docs,
    embedding_model,
    persist_directory="vectorstore"
)

db.persist()

print("All PDFs processed successfully!")