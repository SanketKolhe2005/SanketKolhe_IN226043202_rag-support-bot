from src.loader import load_pdf
from src.vector_store import create_db, get_retriever
from src.qa import generate_answer
from src.graph import build_graph

# Load & process PDF
chunks = load_pdf()

# Create DB
db = create_db(chunks)

# Retriever
retriever = get_retriever(db)

# Graph
graph = build_graph()

print("✅ RAG Support Bot Ready!")

while True:
    query = input("\nAsk your question: ")

    result = graph.invoke({
        "query": query,
        "retriever": retriever,
        "qa": generate_answer
    })

    print("Answer:", result["response"])