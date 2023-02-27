import requests

endpoint = "http://127.0.0.1:8000/user/register/"



# can be changed 
data = {
    "email": "admin@admin.com",
    "first_name":"Shawn",
    "last_name" : "Thiah",
    "user_role": "ADMIN",
    "company": "SMU",
    "designation":"Student",
    "password": "1234"
}

response = requests.post(endpoint,data=data)
print(response.json())