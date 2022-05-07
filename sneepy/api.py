import pyperclip
import os
from .config import Config
from .generator import Generator
import subprocess

config = Config()

class Api:

	def __init__(self):
		self._window = None
	
	def copySnippet(self, code):
		pyperclip.copy(code)

	def setWindow(self, window):
		self._window = window
	
	def minimizeWindow(self):
		self._window.minimize()

	def editFile(self, folder, fileName):
		subprocess.Popen(f'notepad.exe {os.path.join(config.getSnippetsPath(), folder, fileName)}')

	def addSnippet(self, selectedFolder, fileName):
		try:
			open(os.path.join(config.getSnippetsPath(), selectedFolder, fileName), 'w+').close()
			self.editFile(selectedFolder, fileName)
		except Exception as ex:
			return f"Exception occurred: {ex}"
		return ""

	def addFolder(self, folderName):
		try:
			os.mkdir(os.path.join(config.getSnippetsPath(), folderName))
		except Exception as ex:
			return f"Exception occurred: {ex}"
		return ""

	def editSnippet(self, folder, fileName):
		try:
			self.editFile(folder, fileName)
		except Exception as ex:
			return f"Exception occurred: {ex}"
		return ""

	def manageFiles(self):
		subprocess.Popen(f'explorer.exe {os.path.join(config.getSnippetsPath())}')
	
	def reload(self):
		generator = Generator()
		self._window.load_html(generator.generate())
		