import requests
import base64



url = "https://zoom.us/oauth/token"

auth_str = f"{client}:{secret}"
encoded_auth = base64.b64encode(auth_str.encode()).decode()

params = {
    'grant_type': 'refresh_token',
    'refresh_token': refresh_token,
    'redirect_uri': 'https://httpbin.org/get'
}

headers = {
    'Authorization': f'Basic {encoded_auth}',
}
response = requests.post(url, params=params, headers=headers)
response.raise_for_status()

token = response.json().get('access_token')
refresh_token = response.json().get('refresh_token')
val = {'token':token, 'refresh_token':refresh_token}
print(val)

