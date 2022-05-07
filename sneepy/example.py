import os

class Example():

	def createFile(self, file, content):
		fp = open(file, 'w+', encoding='utf-8')
		fp.write(content)
		fp.close()

	def create(self, appRoot):
		os.mkdir(appRoot + 'snippets')
		os.mkdir(appRoot + 'snippets/folder1')
		os.mkdir(appRoot + 'snippets/folder2')
		self.createFile(appRoot + 'snippets/folder1/snippet-1-1.py', 'print("Hello World")')
		self.createFile(appRoot + 'snippets/folder2/snippet-2-1.txt', 'Sneepy rules!')
		self.createFile(appRoot + 'snippets/folder2/snippet-2-2.html', '<b>Hello world</b>')
