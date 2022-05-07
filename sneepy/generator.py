import os
from .config import Config
from .template import Template
from colorama import Fore, Style
import html

config = Config()
template = Template()

class Generator:
	
	def getFolders(self):

		folders = []

		for folder in os.listdir(config.getSnippetsPath()):
			folders.append(folder)
		
		return folders

	def getFiles(self, folder):

		files = []

		for file in os.listdir(os.path.join(config.getSnippetsPath(), folder)):
			files.append(file)
		
		return files
	
	def getFileContent(self, folder, file):
		try:
			fp = open(os.path.join(config.getSnippetsPath(), folder, file), "r", encoding="utf8")
			fileContent = fp.read()
			fp.close()

			return fileContent

		except Exception as ex:
			print(Fore.RED + f'read "{file}": {type(ex).__name__}' + Style.RESET_ALL)
	
	def generate(self):
		snippets = []
		snippetId = 0

		for folder in self.getFolders():

			for file in self.getFiles(folder):
				try:
					code = self.getFileContent(folder, file)
					snippetId += 1
					snippets.append({'id': snippetId, 'title': file, 'folder': folder, 'code': html.escape(code)})
				except Exception as ex:
					print(Fore.RED + f'read "{file}": {type(ex).__name__}' + Style.RESET_ALL)
		
		data = {
			'folders': self.getFolders(),
			'snippets': snippets
		}

		return template.render(data)