#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 26 14:32:23 2018

@author: stoufa
"""

from db import checkDatabase, saveEmbedding, dbConnection

checkDatabase()

lineNumber = 0
with open('../ShakespeareModel.vec') as file:
	for line in file:
		lineNumber += 1
		lineParts = line.split()
		key = lineParts[0]
		del lineParts[0]
		value = ' '.join(lineParts)
		saveEmbedding(key, value)
		print(lineNumber, key)

dbConnection.close()