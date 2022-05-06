import os
from .config import Config
from colorama import Fore, Style
from jinja2 import Template as JinjaTemplate

config = Config()

class Template:

	def getFileContent(self, file):
		try:
			fp = open(os.path.join(config.getAppPath(), 'pwa', file), "r", encoding="utf8")
			fileContent = fp.read()
			fp.close()

			return fileContent

		except Exception as ex:
			print(Fore.RED + f'read "{file}": {type(ex).__name__}' + Style.RESET_ALL)
	
	def render(self, data):
		template = self.getFileContent('template.jinja.html')
		css = self.getFileContent('style.min.css')
		js = self.getFileContent('sneepy.api.js')

		template_data = {
			'folders': data['folders'],
			'snippets': data['snippets'],
			'assets': {
				'css': css,
				'js': js,
			},
			'config': {
				'minimize': config.getValue('autoMinimize'),
			}
		}

		j2_template = JinjaTemplate(template)
		return j2_template.render(template_data)
	
	