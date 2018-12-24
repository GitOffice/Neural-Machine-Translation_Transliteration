# Neural-Machine-Translation_Transliteration
An Intelligent Approach for Translation / Transliteration using Neural Networks

This translation approach is based on Recurrent Neural Networks (RNNs) which are the type of Neural Networks to be used when dealing with sequences of input like videos, sound or text like in our case.

![RNNs](https://camo.githubusercontent.com/c847d37b28afbb2cf3c73bb428354308e16f5efc/68747470733a2f2f63646e2d696d616765732d312e6d656469756d2e636f6d2f6d61782f3830302f312a445537373653477231726859655537696c494b5839772e706e67)

For the data, I used the [bible-corpus](http://christos-c.com/bible/), you have to download the corresponding raw XML files and place them in the directory (`data/bible-corpus/raw/`) then extract the text from these files : you can use the Jupyter Notebook (`word-character embedding/XMLparser.ipynb`) to help you in this task, then save the results in the directory (`data/bible-corpus/pre-processed/`) and finaly run the script (`createEmbeddings.sh`) to generate the embeddings in the directory (`data/bible-corpus/processed/`).

By the way, I used [Fasttext](https://fasttext.cc/) for the embeddings.

The script (`word-character embedding/getEmbedding.py`) reads a word or a character from the user and checks if the embedding is already saved in the SQLite database (`word-character embedding/embeddingDB.db`), otherwise, it computes it using Fasttext even if it's not found in the training corpus! in this case, it will generate the closest embedding based on the word's characters.

The Jupyter Notebook `translate_dev.ipynb` explains the whole pipeline which starts by reading in the training data, tokenization, embedding then building and training the model.
