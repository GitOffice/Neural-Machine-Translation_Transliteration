# Generating Random id’s using UUID in Python
# https://www.geeksforgeeks.org/generating-random-ids-using-uuid-python/

import uuid

class IDgenerator(object):

    @staticmethod
    def newID():
        return str(uuid.uuid4())


if __name__ == '__main__':
    for i in range(5):
        id = IDgenerator.newID()
        print(id)