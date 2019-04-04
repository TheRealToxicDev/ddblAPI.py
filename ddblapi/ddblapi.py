import asyncio
import aiohttp
import json


class DivineAPI:

    def __init__(self, bot_id: int, api_key: str, loop=None, aiosession=None):
        self.bot_id = int(bot_id)
        self.api_key = api_key
        self.loop = loop or asyncio.get_event_loop()
        self.session = aiosession or aiohttp.ClientSession(loop=self.loop)
        self.url = 'https://divinediscordbots.com/bot/{}/stats'
        self.headers = {
            'authorization': self.api_key,
            'content-type': 'application/json'
        }

    async def post_stats(self, server_count: int):
        data = json.dumps({
            'server_count': int(server_count)
        })

        async with self.session.post(self.url.format(self.bot_id), data=data, headers=self.headers) as resp:
            return await self.format_answer(resp)

    async def get_stats(self, user_id: int = None):
        if not user_id:
            user_id = self.bot_id

        async with self.session.get(self.url.format(user_id), headers=self.headers) as resp:
            return await self.format_answer(resp)

    async def format_answer(self, resp):
        return {
            'response': await resp.json(),
            'error': (resp.status != 200),
            'status': resp.status
        }
