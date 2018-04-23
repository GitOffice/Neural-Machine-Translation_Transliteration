# How to return a value from a shell script in a python script
# https://stackoverflow.com/questions/17238263/how-to-return-a-value-from-a-shell-script-in-a-python-script?rq=1

import subprocess
from db import *

# read word / character
inputText = raw_input(">>> ")

checkDatabase()

def cleanEmbedding(embedding):
    embeddingArray = embedding.rstrip().split()

    # remove the first cell (the word/character) corresponding
    # to the embedding vector
    del embeddingArray[0]

    # return the vector as a string (to be stored in the database)
    return ' '.join(embeddingArray)

# check if its embedding is already computed
embeddingFromDB = getEmbedding(inputText)

if len(embeddingFromDB) == 0: # embedding not found in the database
    print('word/character not found in the database !')
    print('computing embedding...')
    # computing the embedding
    embeddingFromScript = subprocess.check_output(['./getEmbedding.sh', inputText])
    embeddingFromScript = cleanEmbedding(embeddingFromScript)
    print("embedding: {}".format(embeddingFromScript))
    saveEmbedding(inputText, embeddingFromScript)

else:   # embedding found in the database
    print('word/character found in the database')
    embeddingFromDB = embeddingFromDB[0] # embeddingFromDB is a tuple containing one element
    print("embedding: {}".format(embeddingFromDB))

dbConnection.close()
