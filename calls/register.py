import requests

endpoint = "http://127.0.0.1:8000/user/register/"



# can be changed 
data = {
    "email": "2em@em.com",
    "first_name":"dan",
    "last_name" : "",
    "user_role": "TECHNICIAN",
    "company": "",
    "designation":"",
    "password": "1234"
}

response = requests.post(endpoint,data=data)
print(response.json())