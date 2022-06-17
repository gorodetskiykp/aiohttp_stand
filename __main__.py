from aiohttp import web

from utils import load_config
from web_app import Application


if __name__ == '__main__':
    config_file = 'config.json'
    config = load_config(config_file=config_file)
    web.run_app(
        app=Application(config),
        host=config.app.host,
        port=config.app.port,
    )