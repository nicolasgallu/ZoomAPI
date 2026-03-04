import requests

with open ("new.csv","r") as f:
    token = f.read()

url = "https://api.zoom.us/v2/report/meetings/7Q+VEoChSzi6bre5fbYB1A==/participants"
headers = {'authorization':f'Bearer {token}'}
next_page_token = ''
params = {"page_size": 10, 'next_page_token': next_page_token}
participants = []

while True:

    response = requests.get(url=url,headers=headers,params=params)
    participants.extend([participant for participant in response.json().get('participants')])
    next_page_token = response.json().get('next_page_token')
    
    if next_page_token:
        params["next_page_token"] = next_page_token
    else:
        break


for i in participants:
    a=i.get('user_email')
    print(a)
    a=i.get('name')
    print(a)
    a=i.get('join_time')
    print(a)
    a=i.get('leave_time')
    print(a)
    a=int(i.get('duration')/60)
    print(a)

#mejorar guardado de ID en base de meeting.
#leer cada meeting id.
#armar condicion de paginado.
#guardar resultados en base de "recorded sessions participants"

##edge functions could work?
##workflow:
#-- refresh token  and 90 days warning over expiring date.
#-- read table recorded sessions and scrapp those listed as "events" and that didnt been tracked yet.
#-- get participants from all recorded sessions and save them in recorded_sessions_participants. if tomorrow one wants to scrap other sessions just need to be in the same previos tag.
