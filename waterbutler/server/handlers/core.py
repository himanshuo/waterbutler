import asyncio

import aiohttp

import tornado.web

from waterbutler import settings
from waterbutler.identity import get_identity
from waterbutler.providers import core


def list_or_value(value):
    assert isinstance(value, list)
    if len(value) == 0:
        return None
    if len(value) == 1:
        return value[0].decode('utf-8')
    return [item.decode('utf-8') for item in value]


class BaseHandler(tornado.web.RequestHandler):

    @asyncio.coroutine
    def prepare(self):
        self.arguments = {
            key: list_or_value(value)
            for key, value in self.request.query_arguments.items()
        }

        self.credentials = yield from get_identity(settings.IDENTITY_METHOD, **self.arguments)

        self.provider = core.make_provider(
            self.arguments['provider'],
            self.credentials
        )

    def write_error(self, status_code, **kwargs):
        self.finish({
            "code": status_code,
            "message": self._reason,
        })
