#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 26 10:53:09 2018

@author: stoufa
"""

from SaveableTST import SaveableTST
from SaveableAVL import SaveableAVL

tstFilepath = 'tst.pickle'
avlFilepath = 'avl.pickle'
vecFilepath = 'ShakespeareModel.vec'
#vecFilepath = 'crawl-300d-2M.vec'

tst = SaveableTST(tstFilepath)
tst.load(createIfNotFound=True)

avl = SaveableAVL(avlFilepath)
avl.load(createIfNotFound=True)

lineNumber = 0
with open(vecFilepath) as vecFile:
	for line in vecFile:
		lineNumber += 1
		lineParts = line.split()
		key = lineParts[0]
		del lineParts[0]
		embedding = ' '.join(lineParts)
		if len(key) == 1:
			# it is a character it should be saved in the AVL
			avl.put(key, embedding)
			print(lineNumber, "key:", key, "--> avl")
		else:
			# otherwise, it is a word, it should be saved in the TST
			tst.put(key, embedding)
			print(lineNumber, "key:", key, "--> tst")
		#print(lineNumber, key)

print("Saving AVL...")
avl.save()

print("Saving TST...")
tst.save()

