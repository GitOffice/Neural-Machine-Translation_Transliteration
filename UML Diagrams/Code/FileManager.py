#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 16:11:21 2018

@author: stoufa

FileManager
--
--
isFileFound(filepath : str) : boolean
isFileNotFound(filepath : str) : boolean

"""

from pathlib import Path

class FileManager():
	
	@staticmethod
	def isFileFound(filepath):
		fileHandler = Path(filepath)
		return fileHandler.exists()
	
	@staticmethod
	def isFileNotFound(filepath):
		return not FileManager.isFileFound(filepath)