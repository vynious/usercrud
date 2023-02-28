# usercrud
CRUD operations of Custom User Models 

python commands of API calls are under "calls" 

API CALLS:

list.py => prompts users to login, if not "ADMIN", action will be not allowed. if "ADMIN" returns with all users in the database

register.py => no permissions, all anyone can register

details.py => prompts the user to login, then user can decide which account detail they will like to retrieve. by default, only "ADMIN" can retrieve details of any user, whereas normal users like "MEMBER" or "TECHNICIAN" can only retrieve their own information.

update.py => prompts login, "ADMIN" can edit anyone's details, other users can only edit their own details. 

delete.py => prompts login, "ADMIN" can delete any accounts, other users can only delete their own by specifying the account to delete which is tag to their email. 





