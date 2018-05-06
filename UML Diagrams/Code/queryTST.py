#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from SaveableTST import SaveableTST
from PickleSaver import PickleSaver

#vecFilepath = 'crawl-300d-2M.vec'
vecFilepath = 'ShakespeareModel.vec'
tstFilepath = f'tst.{vecFilepath}.pickle'

tst = SaveableTST(tstFilepath)
tst.load()

while True:
	inputText = input('>>> ')
	res = tst.get(inputText)
	if res is None:
		print(f'{inputText} is not found!')
	else:
		print(f'{inputText} has the ID {res}')
		emb = PickleSaver.load(f'embeddings/tst.{res}.pickle')
		print(emb)
	print('-'*10)


