import sqlalchemy as sa
from aiohttp import web
from typing import Optional


class BaseProcessingHandler(web.View):

    _table: Optional[sa.Table] = None

    def __init__(self, request: web.Request):
        super().__init__(request)

    @property
    async def current_user(self) -> int:
        return 1

    async def prepare_body(self) -> dict:
        if self.request.can_read_body:
            try:
                return await self.request.json()
            except Exception as exception1:
                raise web.HTTPBadRequest()
        else:
            return {}


class BaseEntityHandler(BaseProcessingHandler):
    async def get(self) -> web.Response:
        entity_id = self.request.match_info.get('id')
        if not entity_id:
            raise AttributeError
        return web.json_response(
            {'head': 'HEAD', 'text': f'text - {entity_id}'}
        )

    async def post(self) -> web.Response:
        entity_id = self.request.match_info.get('id')
        body = await self.prepare_body()
        if not entity_id:
            raise AttributeError
        return web.json_response(
            {'head': 'HEAD', 'text': f'text - {entity_id}'}
        )