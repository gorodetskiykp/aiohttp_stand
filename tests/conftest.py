import pytest

from utils import load_config
from web_app import Application


@pytest.fixture
def app():
    config_file = 'config.json'
    config = load_config(config_file=config_file)
    return Application(config=config)


@pytest.fixture
def client(event_loop, aiohttp_client, app):
    # yield event_loop.run_until_complete(aiohttp_client(app()))
    yield event_loop.run_until_complete(aiohttp_client(app))