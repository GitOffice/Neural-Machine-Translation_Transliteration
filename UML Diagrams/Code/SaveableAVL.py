#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 26 09:46:40 2018

@author: stoufa
"""

from PickleSaver import PickleSaver
from AVL import AVL

class SaveableAVL(object):
	
	def __init__(self, filepath):
		self.filepath = filepath
		self.avl = None
	
	def load(self, createIfNotFound=False):
		if createIfNotFound:
			# create an AVL object and save it
			self.avl = AVL()
			PickleSaver.save(self.avl, self.filepath)
		self.avl = PickleSaver.load(self.filepath)
	
	def save(self):
		PickleSaver.save(self.avl, self.filepath)
	
	def put(self, key, value):
		self.avl.put(key, value)
	
	def remove(self, key):
		self.avl.remove(key)
	
	def get(self, key):
		return self.avl.get(key)


if __name__ == '__main__':
	avl = SaveableAVL('avl.pickle')
	avl.load(True)
	#print(type(avl))
	print(avl.get('a'))
	avl.put('a', [1,2,3])
	print(avl.get('a'))
	avl.save()
	
	avl2 = SaveableAVL('avl.pickle')
	avl2.load()
	print(avl2.get('a'))