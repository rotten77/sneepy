import pathlib
from lxml import etree

class Config:

	def __init__(self):
		self.APP_ROOT = str(pathlib.Path(__file__).parent.parent.absolute())
		self.CONFIG_PATH = self.APP_ROOT + '\sneepy.xml'
	
	def getAppPath(self):
		return self.APP_ROOT
	
	def getValue(self, xpath):
		root = etree.parse(self.CONFIG_PATH)
		element = root.xpath(f'//configuration/{xpath}')[0]

		return element.text
	
	def getSnippetsPath(self):
		snippetspath = self.getValue('snippetsFolder')
		snippetspath = snippetspath.replace("%SNEEPY%", self.APP_ROOT)

		return snippetspath
	
	def getWindowSize(self):
		return [int(self.getValue('window/width')), int(self.getValue('window/height'))]