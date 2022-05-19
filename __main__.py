from sneepy.config import Config
from sneepy.template import Template
from sneepy.api import Api
import webview

template = Template()
config = Config()

html = template.renderLoading()

api = Api()
window_size = config.getWindowSize()
print(window_size)
window = webview.create_window(title=f'Sneepy {config.VERSION}', html=html, js_api=api, width=window_size[0], height=window_size[1])
api.setWindow(window)
webview.start(debug=True, gui='edgechromium')