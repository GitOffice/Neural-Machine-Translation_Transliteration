#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 26 10:53:09 2018

@author: stoufa
"""

from SaveableTST import SaveableTST
from SaveableAVL import SaveableAVL

# Text Progress Bar in the Console
# https://stackoverflow.com/questions/3173320/text-progress-bar-in-the-console

# Print iterations progress
def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█'):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), end = '\r')
    # Print New Line on Complete
    if iteration == total: 
        print()

#vecFilepath = 'ShakespeareModel.vec'
vecFilepath = 'crawl-300d-2M.vec'

tstFilepath = f'tst.{vecFilepath}.pickle'
avlFilepath = f'avl.{vecFilepath}.pickle'

tst = SaveableTST(tstFilepath)
tst.load()

#avl = SaveableAVL(avlFilepath)
#avl.load()

nbTokens = 2000000

# Initial call to print 0% progress
printProgressBar(0, nbTokens, prefix = 'Progress:', suffix = 'Complete', decimals = 2, length = 50)

packetSize = 1000
lineNumber = 0
with open(vecFilepath) as vecFile:
	for line in vecFile:
		lineNumber += 1
		lineParts = line.split()
		key = lineParts[0]
		del lineParts[0]
		embedding = ' '.join(lineParts)
		#if len(key) == 1:
			# it is a character it should be saved in the AVL
			#avl.put(key, embedding)
			#print(lineNumber, "key:", key, "--> avl")
		#else:
			# otherwise, it is a word, it should be saved in the TST
		tst.put(key, embedding)
			#print(lineNumber, "key:", key, "--> tst")
		#print(lineNumber, key)
		if lineNumber % packetSize == 0:
				print("Saving...")
				#avl.save()
				#avl.load()
				tst.save()
				tst.load()
		printProgressBar(lineNumber, nbTokens, prefix = 'Progress:', suffix = 'Complete', decimals = 2, length = 50)

#print("Saving AVL...")
#avl.save()

print("Saving TST...")
tst.save()

