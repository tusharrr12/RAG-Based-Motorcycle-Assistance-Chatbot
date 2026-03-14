from fastapi import FastAPI
from pydantic import BaseModel

from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import SentenceTransformerEmbeddings

from groq import Groq

app = FastAPI()

# Load embedding model
embedding_model = SentenceTransformerEmbeddings(
    model_name="all-MiniLM-L6-v2"
)

# Load vector database
db = Chroma(
    persist_directory="vectorstore",
    embedding_function=embedding_model
)

# Retriever with better search
retriever = db.as_retriever(search_kwargs={"k": 5})

# Groq client
client = Groq(api_key="GROQ_API_KEY")

# Chat memory
chat_history = []


# Detect bike brand
def detect_bike(question):
    bikes = ["ktm", "bajaj", "tvs", "royal enfield", "apache", "duke", "dominar"]

    question = question.lower()

    for bike in bikes:
        if bike in question:
            return bike

    return "motorcycle"


# Request schema
class Question(BaseModel):
    question: str


@app.post("/ask")
def ask_question(q: Question):

    try:

        # Detect bike brand
        bike = detect_bike(q.question)

        # Retrieve relevant docs
        docs = retriever.invoke(q.question)

        print("User question:", q.question)
        print("Detected bike:", bike)
        print("Retrieved docs:", len(docs))

        # Combine context
        context = "\n".join([doc.page_content for doc in docs])

        # Extract sources
        sources = []
        for doc in docs:
            if "source" in doc.metadata:
                sources.append(doc.metadata["source"])

        history_text = "\n".join(chat_history)

        # Prompt
        prompt = f"""
You are an expert motorcycle mechanic specialized in {bike} motorcycles.

Use ONLY the motorcycle manual information.

Previous Conversation:
{history_text}

Manual Context:
{context}

User Question:
{q.question}

Respond in this format:

1. Possible Causes
2. Diagnostic Steps
3. Recommended Fix
4. Safety Advice
"""

        # LLM call
        completion = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": prompt}]
        )

        answer = completion.choices[0].message.content

        # Save conversation
        chat_history.append(f"User: {q.question}")
        chat_history.append(f"Assistant: {answer}")

        return {
            "question": q.question,
            "bike_detected": bike,
            "answer": answer,
            "sources": list(set(sources))
        }

    except Exception as e:
        print("ERROR:", e)
        return {"error": str(e)}