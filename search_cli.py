import json
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
import time

# --- Configuration ---
processed_json_file = 'data.json'
index_file = 'emoji_index.faiss'
# --- MODEL UPGRADE (Must match the one used for indexing) ---
model_name = 'all-mpnet-base-v2'

def run_search_app():
    print("--- Initializing Emoji Search Engine ---")
    
    print(f"Loading emoji data...")
    with open(processed_json_file, 'r', encoding='utf-8') as f:
        emoji_data = json.load(f)
        
    print(f"Loading FAISS index...")
    index = faiss.read_index(index_file)
    
    print(f"Loading embedding model: '{model_name}'...")
    model = SentenceTransformer(model_name, device='cpu')
    
    print("\n✅ Search engine is ready!")
    print("--------------------------------------------------")

    while True:
        query = input("Enter a search query (or type 'exit' to quit): ")
        if query.lower() == 'exit': break
        if not query: continue
        
        start_time = time.time()
        
        # --- CRITICAL FIX ---
        # Normalize the query embedding just like the index embeddings.
        query_embedding = model.encode([query], normalize_embeddings=True)
        
        top_k = 5 
        distances, indices = index.search(query_embedding.astype('float32'), top_k)
        end_time = time.time()
        
        print(f"\nTop {top_k} results for '{query}' (found in {end_time - start_time:.4f} seconds):")
        
        for i in range(top_k):
            result_index = indices[0][i]
            retrieved_emoji = emoji_data[result_index]
            similarity_score = distances[0][i]
            
            print(f"  {i+1}. {retrieved_emoji['emoji']} {retrieved_emoji['title']} (Similarity: {similarity_score:.4f})")

        print("--------------------------------------------------")

if __name__ == "__main__":
    run_search_app()
