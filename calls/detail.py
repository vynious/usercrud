import requests
from getpass import getpass

# authenticating users (aka login function)

auth_endpoint = 'http://127.0.0.1:8000/api/token/'
email = input('email: ')
password = getpass()
data = {
    'email': email,
    'password': password,
}
auth_response = requests.post(auth_endpoint, data=data)

# fetch account details 



# API Call to fetch the target account 

if auth_response.status_code == 200:
    query = input('Account details of ==> ')
    token = auth_response.json()['access']
    header = {
        'Authorization':f'Bearer {token}'
    }
    data = {
        'email' : query,
    }
    endpoint = 'http://127.0.0.1:8000/user/detail/'
    response = requests.get(endpoint,headers=header, data=data)
    print(response.json())
else:
    print('Try again, something went wrong...')