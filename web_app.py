from aiohttp import web
from routes import letter_routes


class Application(web.Application):

    def __init__(self, config, **kwargs):
        super().__init__(**kwargs)
        self.config = config
        self._prepare_app()
        self['init'] = True

    def _prepare_app(self):
        self._setup_routes()

    def _setup_routes(self):
        self.add_routes(letter_routes)