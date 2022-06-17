import pytest
import aiohttp
from aiohttp import web

from config_model import MainConfig
from handler.letter_handler import LetterEntityHandler


routes = [
    '/api/Letter/1',
    '/api/Letter/2',
    '/api/fLetter/1',
    '/api/fLetter/2'
]


@pytest.mark.parametrize('route', routes)
async def test_routes(client, route):
    resp = await client.get(route)
    assert resp.status == 200
    text = await resp.text()
    assert route[-1] in text
    resp = await client.post(route)
    assert resp.status == 200


async def test_letter_handler(client):
    letter = LetterEntityHandler(web.Request)
    user = await letter.current_user
    assert user == 1
    body = await letter.prepare_body()
    assert type(body) == dict


async def test_start_app(app, client):
    assert isinstance(app, web.Application)
    assert isinstance(app.config, MainConfig)
    assert app.config.app.__class__.__name__ == 'WebAppConfig'
    assert app['init'] == True
    assert client.server.app['init'] == True