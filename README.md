# neural-machine-translation_transliteration
an intelligent approach for translation / transliteration using neural networks

For the data, I used the [bible-corpus](http://christos-c.com/bible/), you have to download the corresponding raw XML files and place them in the directory (`data/bible-corpus/raw/`) then extract the text from these files : you can use the jupyter notebook (`word-character embedding/XMLparser.ipynb`) to help you in this task, then save the results in the directory (`data/bible-corpus/pre-processed/`) and finaly run the script (`createEmbeddings.sh`) to generate the embeddins in the directory (`data/bible-corpus/processed/`).

By the way, I used [Fasttext](https://fasttext.cc/) for the embeddings.

The script (`word-character embedding/getEmbedding.py`) reads a word or a character from the user and checks if the embedding is already saved in the SQLite database (`word-character embedding/embeddingDB.db`), otherwise, it computes it using Fasttext even if it's not found in the training corpus ! in this case, it will generate the closest embedding based on the word's characters.

