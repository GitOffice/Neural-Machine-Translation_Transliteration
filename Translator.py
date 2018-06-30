#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  4 00:39:26 2018

@author: stoufa
"""

from Tokenizer import Tokenizer

class Translator(object):
	
	def __init__(self):
		pass

	@staticmethod
	def translate(inputText):
		tokens = Tokenizer.tokenize(inputText)
		#tokensEmbeddings = map(Embedder.embed, tokens)
		#return list(tokensEmbeddings)
		
		# pass the embeddings through the neural network and get the results
		# unembed the translated words' embedding vectors to words
		# untokenize the translated tokens !
		
		return Tokenizer.untokenize(tokens)

if __name__ == '__main__':
	text = input('>>> ')
	
	# Translating
	translatedText = Translator.translate(text)
	print(f'translatedText: {translatedText}')
