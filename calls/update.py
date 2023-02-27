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
    changes = {'account' : 'shawn@test.com',}
    while True:
        change = input('specify field of change (else => N): ')
        if change == 'N':
            break
        else:
            new_value = input(f'what is the updated {change}: ')
            changes[change] = new_value

    endpoint = 'http://127.0.0.1:8000/user/update/'
    response = requests.post(endpoint,headers=header, data=changes)

    print(response.json())