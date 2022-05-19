import os
from .config import Config
from .template import Template
import html

config = Config()
template = Template()

class Generator:
	"""Snippets generator"""
	
	def getFolders(self):

		folders = []

		for folder in os.listdir(config.getSnippetsPath()):
			folders.append(folder)
		
		return folders
	
	def getFileExtension(self, file):
		ext = os.path.splitext(file)[1]
		return ext[1:]

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
			print(f'read "{file}": {type(ex).__name__}')
	
	def generate(self):
		snippets = []
		snippetId = 0

		for folder in self.getFolders():

			for file in self.getFiles(folder):
				try:
					code = self.getFileContent(folder, file)
					snippetId += 1
					snippets.append({'id': snippetId, 'title': file, 'folder': folder, 'code': html.escape(code), 'ext': self.getFileExtension(file)})
				except Exception as ex:
					print(f'read "{file}": {type(ex).__name__}')
		
		data = {
			'folders': self.getFolders(),
			'snippets': snippets
		}

		return template.render(data)