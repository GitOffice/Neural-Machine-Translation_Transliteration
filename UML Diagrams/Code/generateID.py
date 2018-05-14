import time
import uuid

# Generating Random id’s using UUID in Python
# https://www.geeksforgeeks.org/generating-random-ids-using-uuid-python/

def generateId():
    #return str(time.time())
    #return uuid.uuid1()
    return uuid.uuid4()

if __name__ == '__main__':
    for i in range(5):
        print(generateId())
        # generating IDs using timestamps is a bad idea ! we can easily have conflits if the processing is so quick !
        # using the module uuid is the best solution, uuid.uuid4() is the best option

