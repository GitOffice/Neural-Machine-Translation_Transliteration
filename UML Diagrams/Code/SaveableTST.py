#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 26 09:46:40 2018

@author: stoufa
"""

from PickleSaver import PickleSaver
from TST import TST

class SaveableTST(object):
	
	def __init__(self, filepath):
		self.filepath = filepath
		self.tst = None
	
	def load(self):
		try:
			# if the file exists, load it
			self.tst = PickleSaver.load(self.filepath)
		except FileNotFoundError:
			# else create a new instance and save it
			self.tst = TST()
			PickleSaver.save(self.tst, self.filepath)
	
	def save(self):
		PickleSaver.save(self.tst, self.filepath)
	
	def put(self, key, value):
		self.tst.put(key, value)
		# save the embedding in a file
		PickleSaver.save(value, f'embeddings/tst.{TST.NbInstances}.pickle')
	
	def remove(self, key):
		self.tst.remove(key)
	
	def get(self, key):
		return self.tst.get(key)


if __name__ == '__main__':
	tst = SaveableTST('tst.pickle')
	tst.load()
	#print(type(avl))
	print(tst.get('abc'))
	tst.put('abc', [1,2,3])
	print(tst.get('abc'))
	tst.save()
	
	tst2 = SaveableTST('tst.pickle')
	tst2.load()
	print(tst2.get('abc'))