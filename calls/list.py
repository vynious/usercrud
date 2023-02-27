import requests
from getpass import getpass

endpoint = 'http://127.0.0.1:8000/user/'
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
    response = requests.get(endpoint,headers=header)
    print(response.json())
