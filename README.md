## EmojiSearch 🔎

**EmojiSearch** simplifies finding the perfect emoji, making the process much faster.

### **Try It Out**

You can use the web interface here:
**[Hugging Face Space](https://huggingface.co/spaces/TanishkB/emojisearch/)**

### **Command Line Usage**

1.  Run the CLI:
    ```bash
    python search_cli.py
    ```
2.  Type your search query.

### **Vector Databases & Performance**

The search utility uses four different vector databases, allowing you to switch between models by updating the `index_file` and `processed_json_file` in the `search_cli.py` config.

| Rank | Model Name | Index File | Performance Note |
| :---: | :--- | :--- | :--- |
| **1** | **`all-mpnet-base-v2`** | `emoji_index.faiss` | **Recommended** (Best at "guessing" emojis) |
| 2 | `BAAI/bge-base-en-v1.5` | `emoji_index_BAAI.faiss` | Good alternative |
| 3 | `google/embeddinggemma-300M` | `emoji_index_gemma.faiss` | Less effective |
| 4 | `Qwen/Qwen3-Embedding-0.6B` | `emoji_index_qwen.faiss` | Less effective |

*Note: Models 3 & 4 are currently less effective, possibly due to they are generalist embedding models.*
