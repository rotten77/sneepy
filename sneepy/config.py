from lxml import etree
import sys
from .example import Example
from os import path

example = Example()

class Config:
	"""Configuration"""

	VERSION = '1.1.0.2'

	def __init__(self):
		self.APP_ROOT = './'
		self.CONFIG_PATH = self.APP_ROOT + 'sneepy.xml'

		# Generate configuration file if not exists
		if not path.isfile(self.CONFIG_PATH):
			configuration = etree.Element('configuration')
			snippetsFolder = etree.SubElement(configuration, 'snippetsFolder')
			snippetsFolder.text = 'snippets'

			autoMinimize = etree.SubElement(configuration, 'autoMinimize')
			autoMinimize.text = 'false'

			window = etree.SubElement(configuration, 'window')
			width = etree.SubElement(window, 'width')
			width.text = '960'
			height = etree.SubElement(window, 'height')
			height.text = '720'

			config_xml = etree.ElementTree(configuration)
			config_xml.write(self.CONFIG_PATH, pretty_print=True, xml_declaration=True, encoding='UTF-8')
		
		# Generate snippet folders if not exist
		snippetstPath = self.getSnippetsPath()
		if snippetstPath == "snippets":
			if not path.isdir(snippetstPath):
				example.create(self.APP_ROOT)
	
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
		return self.getValue('snippetsFolder')
	
	def getWindowSize(self):
		return [int(self.getValue('window/width')), int(self.getValue('window/height'))]