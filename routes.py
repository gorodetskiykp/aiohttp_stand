from aiohttp import web

from handler.letter_handler import letter_entity_handler, LetterEntityHandler


letter_routes = [
    web.view(r'/api/Letter/{id:\d+}', letter_entity_handler),
    web.view(r'/api/fLetter/{id:\d+}', LetterEntityHandler),
]