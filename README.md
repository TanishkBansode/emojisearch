# EmojiSearch

Makes searching emojis extremely easier.

Just run `python search_cli.py` and then type your query.
There are two vector databases, for 2 different models:
1. all-mpnet-base-v2 - emoji_index.faiss
2. BAAI/bge-base-en-v1.5 - emoji_index_BAAI.faiss

so just change the index_file and processed_json_file in config of `search_cli.py`
imo first one is better.
