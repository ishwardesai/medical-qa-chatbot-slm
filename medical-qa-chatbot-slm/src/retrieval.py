"""
RAG Retrieval System
Semantic search using SentenceTransformers + FAISS.
Upgraded from TF-IDF baseline in SLM document to neural embeddings.
"""

from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

class MedicalRetriever:
    def __init__(self, documents: list):
        self.documents = documents
        self.corpus = [doc['content'] for doc in documents]
        self.titles = [doc['title'] for doc in documents]
        
        print("Loading sentence transformer...")
        self.embedder = SentenceTransformer('all-MiniLM-L6-v2')
        
        print("Building FAISS index...")
        embeddings = self.embedder.encode(
            self.corpus,
            normalize_embeddings=True,
            show_progress_bar=True
        )
        embeddings = np.array(embeddings, dtype='float32')
        
        dimension = embeddings.shape[1]
        self.index = faiss.IndexFlatIP(dimension)
        self.index.add(embeddings)
        print(f"✓ Index built: {self.index.ntotal} documents")
    
    def retrieve(self, query: str, top_k: int = 3) -> list:
        """Retrieve top-k most relevant documents for query"""
        query_embedding = self.embedder.encode(
            [query], normalize_embeddings=True
        )
        query_embedding = np.array(query_embedding, dtype='float32')
        
        scores, indices = self.index.search(query_embedding, top_k)
        
        results = []
        for score, idx in zip(scores[0], indices[0]):
            results.append({
                'title': self.titles[idx],
                'content': self.corpus[idx],
                'score': float(score)
            })
        return results
