from sneepy.config import Config
from sneepy.generator import Generator
from sneepy.api import Api
import webview

generator = Generator()
config = Config()
html = generator.generate()

api = Api()
window_size = config.getWindowSize()
print(window_size)
window = webview.create_window(title=f'Sneepy {config.VERSION}', html=html, js_api=api, width=window_size[0], height=window_size[1])
api.setWindow(window)
webview.start(debug=True, gui='edgechromium')