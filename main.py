import requests
import re


def validate_discord_token(token):
    # Regular expression to check the token format
    if not re.match(r'^[A-Za-z0-9]{24}\.[A-Za-z0-9]{6}\.[A-Za-z0-9_\-\.]$', token):
        return False

    url = 'https://discord.com/api/v10/users/@me'
    headers = {'Authorization': token}

    response = requests.get(url, headers=headers)
    return response.status_code == 200


token = 'YOUR_BOT_TOKEN_HERE'
if validate_discord_token(token):
    print('Valid token.')
else:
    print('Invalid token.')
