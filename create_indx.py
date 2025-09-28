import json
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
import time

# --- Configuration ---
processed_json_file = 'data.json'
index_file = 'emoji_index.faiss'
# --- MODEL UPGRADE ---
model_name = 'BAAI/bge-base-en-v1.5' # A more powerful model for semantic search

def create_and_save_index():
    print(f"Loading data from '{processed_json_file}'...")
    with open(processed_json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    emoji_texts = [item['combined_text'] for item in data]
    print(f"Found {len(emoji_texts)} emoji texts.")

    print(f"Loading the embedding model: '{model_name}'...")
    model = SentenceTransformer(model_name, device='cpu')
    
    print("Generating embeddings...")
    start_time = time.time()
    
    # --- CRITICAL FIX ---
    # Ensure normalization is enabled to make vectors comparable via cosine similarity.
    embeddings = model.encode(emoji_texts, normalize_embeddings=True, show_progress_bar=True)

    end_time = time.time()
    print(f"Embedding generation completed in {end_time - start_time:.2f} seconds.")

    print("Building the FAISS index...")
    embedding_dimension = embeddings.shape[1]
    index = faiss.IndexFlatIP(embedding_dimension)
    index.add(embeddings.astype('float32'))
    
    print(f"Saving the index to '{index_file}'...")
    faiss.write_index(index, index_file)
    print("\n✅ Index created successfully with the new model.")

if __name__ == "__main__":
    create_and_save_index()
