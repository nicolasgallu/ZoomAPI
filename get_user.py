import requests

with open ("new.csv","r") as f:
    token = f.read()

url = "https://api.zoom.us/v2/users/me/settings"
headers = {'authorization':f'Bearer {token}'}
response = requests.get(url=url,headers=headers)
print(response.json())
