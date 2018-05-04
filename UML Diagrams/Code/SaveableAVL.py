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
	
	def load(self):
		try:
			# if the file exists, load it
			self.avl = PickleSaver.load(self.filepath)
		except FileNotFoundError:
			# else create a new instance and save it
			self.avl = AVL()
			PickleSaver.save(self.avl, self.filepath)
	
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
	avl.load()
	#print(type(avl))
	print(avl.get('a'))
	avl.put('a', [1,2,3])
	print(avl.get('a'))
	avl.save()
	
	avl2 = SaveableAVL('avl.pickle')
	avl2.load()
	print(avl2.get('a'))