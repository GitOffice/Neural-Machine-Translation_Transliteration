#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  2 23:49:05 2018

@author: stoufa
"""

from Tokenizer import Tokenizer

class Embedder(object):
	
	@staticmethod
	def embed(token):
		if Embedder.isCharacter(token):
			return AVL.getInstance().getEmbedding(token)
		else:
			return TST.getInstance().getEmbedding(token)

	@staticmethod
	def isCharacter(token):
		return len(token) == 1
	
	# implement unembed here !

# Both AVL and TST are implementing the Singleton Design Pattern
class AVL(object):
	
	instance = None
	
	@staticmethod
	def getInstance():
		if AVL.instance is None:
			AVL.instance = AVL()
		return AVL.instance
	
	def getEmbedding(self, token):
		return [1, 2, 3]


class TST(object):
	
	instance = None
	
	@staticmethod
	def getInstance():
		if TST.instance is None:
			TST.instance = TST()
		return TST.instance
	
	def getEmbedding(self, token):
		return [3, 2, 1]


if __name__ == '__main__':
	text = input('>>> ')
	tokens = Tokenizer.tokenize(text)
	print(f'tokens: {tokens}')
	for token in tokens:
		embedding = Embedder.embed(token)
		print(token, embedding)

