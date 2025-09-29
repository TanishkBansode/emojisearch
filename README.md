# EmojiSearch

Makes searching emojis extremely easier.

Just run `python search_cli.py` and then type your query.
There are four vector databases, for 4 different models:
(They are ranked based on their ability to 'guess' the emojis)
1. all-mpnet-base-v2 - emoji_index.faiss
2. BAAI/bge-base-en-v1.5 - emoji_index_BAAI.faiss

(Almost unusable, my current theory suggests that it might be because they are generalist models, and made to do a wide range of tasks)
3. google/embeddinggemma-300M - emoji_index_gemma.faiss
4. Qwen/Qwen3-Embedding-0.6B - emoji_index_qwen.faiss
\
so just change the index_file and processed_json_file in config of `search_cli.py`
imo first one is better.
