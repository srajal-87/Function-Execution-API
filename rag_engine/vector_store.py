import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

class FunctionVectorStore:
    def __init__(self, model_name='all-MiniLM-L6-v2'):
        self.embedding_model = SentenceTransformer(model_name)
        self.function_metadata = []
        self.vector_index = None
    
    def add_function(self, function_name, description):
        """Add function metadata to the vector store"""
        embedding = self.embedding_model.encode([description])[0]
        self.function_metadata.append({
            "name": function_name,
            "description": description
        })
        
        if self.vector_index is None:
            self.vector_index = faiss.IndexFlatL2(embedding.shape[0])
        
        self.vector_index.add(np.array([embedding]))
    
    def retrieve_function(self, query, top_k=1):
        """Retrieve most similar function based on query"""
        query_embedding = self.embedding_model.encode([query])[0]
        distances, indices = self.vector_index.search(np.array([query_embedding]), top_k)
        
        return [self.function_metadata[idx] for idx in indices[0]]