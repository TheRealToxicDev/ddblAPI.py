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
        url = f'https://divinediscordbots.com/bot/{self.bot_id}/stats'

        async with aiohttp.ClientSession() as session:
            async with session.post(url, data=data, headers=self.headers) as resp:
                if resp.status == 200:
                    return {
                        'response': 'ServerCount Successfully posted  !',
                        'error': False,
                        'status': resp.status
                    }
                else:
                    error_json = await resp.json()
                    return {
                        'response': error_json['error'],
                        'error': True,
                        'status': resp.status
                    }

    async def get_stats(self, user_id):
        if not int(user_id):
            user_id = self.bot_id

        url = f'https://divinediscordbots.com/bot/{user_id}/stats'

        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=self.headers) as resp:
                if resp.status == 200:
                    return {
                        'response': await resp.json(),
                        'error': False,
                        'status': resp.status
                    }

                else:
                    error_json = await resp.json()
                    return {
                        'response': error_json['error'],
                        'error': True,
                        'status': resp.status
                    }
