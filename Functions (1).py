import io
import os
from pathlib import Path

import sys
from Globals import *

def makeFile(fileFullPath, fileContent):
	# First Check if path exists
	dirPath = os.path.dirname(fileFullPath)
	directory = Path(dirPath)
	if directory.is_dir():
		print(dirPath + " exists.")
	else:
		makeDirectory(dirPath)
		print(dirPath + " does NOT exist.")

def makeDirectory(directoryFullPath):
	parentPath = os.path.dirname(directoryFullPath)

	parentDirectory = Path(parentPath)
	if parentDirectory.is_dir():
		print(parentPath + " exists")
	else:
		print(parentPath + " does NOT exists")

# makeFile(ROOT_PATH + '/data/Persons.json', 'Empty File')
