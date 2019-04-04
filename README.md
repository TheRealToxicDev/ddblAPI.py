# ddblAPI.py
The official python wrapper of Divine Discord Bot List

### Requirements
- [**+Python3**](https://www.python.org/downloads/)
- [**aiohttp**](https://pypi.org/project/aiohttp/)

### Installation
Using **pip**:
```
sudo pip install pyddblapi
```


### Example usage

```py
import discord
from ddblapi import DivineAPI

bot_id = '' # Your Bot ID
bot_token = '' # Your Bot token
api_key = '' # Your bot divinediscordbots.com API_KEY

ddbl = DivineAPI(bot_id=bot_id, api_key=api_key)


class Bot(discord.Client):

    async def on_ready(self):
        server_count = len(self.guilds)
        post_stats = await ddbl.post_stats(server_count)

        if post_stats['error']:
            print(f'An error has occured with status {post_stats["status"]}:\n{post_stats["response"]}')
        else:
            print(f'Successfully posted stats on Divine Discord Bot List with status {post_stats["status"]} !')


Bot().run(bot_token)
```
