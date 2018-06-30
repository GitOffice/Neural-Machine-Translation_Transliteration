import sqlite3

dbFilename = 'embeddingDB.db'
dbConnection = sqlite3.connect(dbFilename)
dbCursor = dbConnection.cursor()

def getEmbedding(input):
    """
    returns the embedding of the input word / character if it is found in the database, returns an empty list otherwise
    """
    dbCursor.execute("SELECT embedding FROM embeddings WHERE input=:inputPlaceholder", {'inputPlaceholder': input})
    resultList = dbCursor.fetchall()
    if len(resultList) != 0:
        # we have one embedding per word/character, .fetchall() returns a list
        result = resultList[0]
    else:
        result = []
    return result

def saveEmbedding(input, embedding):
    """
    saves the embedding of the input word / character to the database
    """
    with dbConnection:
        dbCursor.execute("INSERT INTO embeddings VALUES (:inputPlaceholder, :embeddingPlaceholder)", {'inputPlaceholder': input, 'embeddingPlaceholder': embedding})

def checkDatabase():
    # How do I check in SQLite whether a table exists?
    # https://stackoverflow.com/questions/1601151/how-do-i-check-in-sqlite-whether-a-table-exists
    # if the database file is not found
    dbCursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=:tableName", {'tableName': 'embeddings'})
    tableExists = len( dbCursor.fetchall() ) != 0
    if not tableExists:
        # create it
        dbCursor.execute("""CREATE TABLE embeddings (
                            input text,
                            embedding text
                            )""")
        # create a column index on input ( to make the lookup faster )
        # https://www.tutorialspoint.com/sqlite/sqlite_indexes.htm
        dbCursor.execute("""CREATE INDEX input_index ON embeddings (input);""")


