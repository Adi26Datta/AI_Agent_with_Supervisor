from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Neo4jVector
from dotenv import load_dotenv
import os

load_dotenv()

# Function to query the vector store
def query_vector_rag(question: str, top_k: int = 3):
    print(f"Querying vector store with question: {question}")
    vector_store = Neo4jVector.from_existing_graph(
        embedding=OpenAIEmbeddings(),
        url=os.getenv("NEO4J_URI"),
        username=os.getenv("NEO4J_USERNAME"),
        password=os.getenv("NEO4J_PASSWORD"),
        index_name='Chunk',
        node_label='Chunk',
        text_node_properties=['text'],
        embedding_node_property='textEmbeddingOpenAI',
    )
    docs_and_scores = vector_store.similarity_search_with_score(
        question, 
        k=3
    )
    print(f"Found {len(docs_and_scores)} documents with scores.")
    return docs_and_scores

