# neural-machine-translation_transliteration
an intelligent approach for translation / transliteration using neural networks

For the data, I used the [bible-corpus](http://christos-c.com/bible/), I worked with 3 languages namely: English, French and Arabic, and I used [Fasttext](https://fasttext.cc/) for the embeddings. The raw data is in XML format, I used the jupyter notebook (`word-character embedding/XMLparser.ipynb`) to process it.

The script (`word-character embedding/getEmbedding.py`) reads a word or a character from the user and checks if the embedding is already saved in the SQLite database (`word-character embedding/embeddingDB.db`), otherwise, it computes it using Fasttext (even if it's not found in the corpus ! in this case, it will generate the closest embedding based on its characters).

