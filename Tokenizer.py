#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  2 23:39:00 2018

@author: stoufa
"""

class Tokenizer(object):
	
	@staticmethod
	def tokenize(text):
		#print(f'tokenizing: {text}')
		return text.split()

	@staticmethod
	def untokenize(tokens):
		#print(f'untokenizing: {tokens}')
		return ' '.join(tokens)

if __name__ == '__main__':
	text = input('>>> ')
	
	# Tokenizing
	tokens = Tokenizer.tokenize(text)
	print(f'tokens: {tokens}')
	
	# UnTokenizing
	untokenizedText = Tokenizer.untokenize(tokens)
	print(f'untokenizedText: {untokenizedText}')