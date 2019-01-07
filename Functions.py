import io
import os
from pathlib import Path

import sys
from Global import *

def makeFile(fileFullPath, fileContent):
	# First Check if path exists
	dirPath = os.path.dirname(fileFullPath)
	directory = Path(dirPath)
	if  not directory.is_dir():
		makeDirectory(dirPath)

	writer = open(fileFullPath, "w")
	writer.write(fileContent)
	writer.close()

def makeDirectory(directoryFullPath):
	parentPath = os.path.dirname(directoryFullPath)

	parentDirectory = Path(parentPath)
	if  not parentDirectory.is_dir():
		makeDirectory(parentPath)

	os.makedirs(directoryFullPath)
	return

def convertNone(str):
	# if (str == 'None'):
		# return None
	return str