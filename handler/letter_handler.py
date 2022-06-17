from aiohttp import web

from handler.base_handler import BaseEntityHandler


async def letter_entity_handler(request):
    letter_id = request.match_info['id']
    return web.Response(text=f"Вам письмо! - {letter_id}")


class LetterEntityHandler(BaseEntityHandler):
    pass