#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 16:02:06 2018

@author: stoufa

PickleSaver
--
--
_save(objectToBeSaved, filepath)_
_load(filepath) : object_

"""

import pickle
from FileManager import FileManager

class PickleSaver():
	
	@staticmethod
	def save(objectToBeSaved, filepath):
		with open(filepath, 'wb') as pickleFile:
			# w:write, b:binary
			objectToBeSavedAsString = pickle.dumps(objectToBeSaved)
			pickleFile.write(objectToBeSavedAsString)
	
	@staticmethod
	def load(filepath):
		if FileManager.isFileNotFound(filepath):
			raise FileNotFoundError('{} is not found!'.format(filepath))

		with open(filepath, 'rb') as pickleFile:
			# r:read, b:binary
			objectToBeLoadedAsString = pickleFile.read()
			loadedObject = pickle.loads(objectToBeLoadedAsString)
		return loadedObject
