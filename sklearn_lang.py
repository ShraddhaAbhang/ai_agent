from langchain.chains import RetrievalQA
from langchain.vectorstores import FAISS
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

# Sample data: Replace this with your own knowledge base
documents = [
    "LangChain is a framework for developing applications powered by language models.",
    "scikit-learn is a machine learning library for Python.",
    "FAISS is a library for efficient similarity search and clustering of dense vectors.",
    "You can build chatbots and other applications using LangChain.",
]

# Step 1: Define the embedding model using TfidfVectorizer
class TfidfRetriever:
    def __init__(self, documents):
        self.vectorizer = TfidfVectorizer()
        self.document_vectors = self.vectorizer.fit_transform(documents).toarray()
        self.documents = documents

    def retrieve(self, query, top_k=1):
        query_vector = self.vectorizer.transform([query]).toarray()
        similarities = np.dot(self.document_vectors, query_vector.T).flatten()
        top_indices = similarities.argsort()[-top_k:][::-1]
        return [(self.documents[i], similarities[i]) for i in top_indices]

# Step 2: Implement a simple QA retrieval logic
class SimpleQA:
    def __init__(self, retriever):
        self.retriever = retriever

    def ask(self, question):
        retrieved_docs = self.retriever.retrieve(question, top_k=1)
        if retrieved_docs:
            return retrieved_docs[0][0]
        return "I don't know the answer to that."

# Step 3: Set up the retriever and QA system
retriever = TfidfRetriever(documents)
qa_system = SimpleQA(retriever)

# Step 4: Interact with the AI agent
while True:
    user_input = input("Ask a question (type 'exit' to quit): ")
    if user_input.lower() == 'exit':
        break
    answer = qa_system.ask(user_input)
    print(f"Answer: {answer}")
