import aiohttp
import json


class DivineAPI:

    def __init__(self, bot_id, api_key):
        self.bot_id = int(bot_id)
        self.api_key = api_key
        self.headers = {
            'authorization': self.api_key,
            'content-type': 'application/json'
        }

    async def post_stats(self, server_count):
        data = json.dumps({
            'server_count': int(server_count)
        })
        url = 'https://divinediscordbots.com/bot/{}/stats'.format(self.bot_id)

        async with aiohttp.ClientSession() as session:
            async with session.post(url, data=data, headers=self.headers) as resp:
                if resp.status == 200:
                    return {
                        'response': 'ServerCount Successfully posted  !',
                        'error': (resp.status == 200),
                        'status': resp.status
                    }
                else:
                    error_json = await resp.json()
                    return {
                        'response': error_json['error'],
                        'error': (resp.status == 200),
                        'status': resp.status
                    }

    async def get_stats(self, user_id):
        url = 'https://divinediscordbots.com/bot/{}/stats'.format(user_id)

        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=self.headers) as resp:
                if resp.status == 200:
                    return {
                        'response': await resp.json(),
                        'error': (resp.status == 200),
                        'status': resp.status
                    }
                else:
                    error_json = await resp.json()
                    return {
                        'response': error_json['error'],
                        'error': (resp.status == 200),
                        'status': resp.status
                    }
