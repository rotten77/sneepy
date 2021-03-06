import os
from .config import Config
from jinja2 import Template as JinjaTemplate

config = Config()

class Template:
	"""Template renderer"""

	def getFileContent(self, file):
		try:
			fp = open(os.path.join(config.getAppPath(), 'pwa', file), "r", encoding="utf8")
			fileContent = fp.read()
			fp.close()

			return fileContent

		except Exception as ex:
			print(f'read "{file}": {type(ex).__name__}')
	
	def renderLoading(self):
		template = self.getFileContent('loading.html.jinja')
		css = self.getFileContent('style.min.css')
		js = self.getFileContent('sneepy.api.js')

		template_data = {
			'assets': {
				'css': css,
				'js': js,
			},
			'config': {
				'minimize': config.getValue('autoMinimize'),
				'version': config.VERSION,
			}
		}

		j2_template = JinjaTemplate(template)
		return j2_template.render(template_data)

	def render(self, data):
		template = self.getFileContent('template.html.jinja')
		css = self.getFileContent('style.min.css')
		js = self.getFileContent('sneepy.api.js')
		prism_js = self.getFileContent('prism.js')
		prism_css = self.getFileContent('prism.css')

		template_data = {
			'folders': data['folders'],
			'snippets': data['snippets'],
			'assets': {
				'css': css,
				'js': js,
				'prism': {
					'css': prism_css,
					'js': prism_js,
				}
			},
			'config': {
				'minimize': config.getValue('autoMinimize'),
				'version': config.VERSION,
			}
		}

		j2_template = JinjaTemplate(template)
		return j2_template.render(template_data)
	
	