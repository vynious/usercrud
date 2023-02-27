import requests
from getpass import getpass


auth_endpoint = 'http://127.0.0.1:8000/api/token/'
email = input('email: ')
password = getpass()
data = {
    'email': email,
    'password': password,
}
auth_response = requests.post(auth_endpoint, data=data)


if auth_response.status_code == 200:
    token = auth_response.json()['access']
    header = {
        'Authorization':f'Bearer {token}'
    }
    data = {
        'email' : email,
    }
    endpoint = 'http://127.0.0.1:8000/user/delete/'
    response = requests.delete(endpoint,headers=header, data=data)
    print(response.json())
