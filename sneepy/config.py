from lxml import etree
import sys

class Config:

	def __init__(self):
		self.APP_ROOT = './'
		self.CONFIG_PATH = self.APP_ROOT + 'sneepy.xml'
	
	def getAppPath(self):
		if getattr(sys, 'frozen', False):
			return sys._MEIPASS
		else:
			return self.APP_ROOT

	
	def getValue(self, xpath):
		root = etree.parse(self.CONFIG_PATH)
		element = root.xpath(f'//configuration/{xpath}')[0]

		return element.text
	
	def getSnippetsPath(self):
		snippetspath = self.getValue('snippetsFolder')

		return snippetspath
	
	def getWindowSize(self):
		return [int(self.getValue('window/width')), int(self.getValue('window/height'))]