# usercrud
CRUD operations of Custom User Models 

python commands of API calls are under "calls" 

## API CALLS:

list.py => prompts users to login, if not "ADMIN", action will be not allowed. if "ADMIN" returns with all users in the database

register.py => no permissions, all anyone can register

details.py => prompts the user to login, then user can decide which account detail they will like to retrieve. by default, only "ADMIN" can retrieve details of any user, whereas normal users like "MEMBER" or "TECHNICIAN" can only retrieve their own information.

update.py => prompts login, "ADMIN" can edit anyone's details, other users can only edit their own details. 

delete.py => prompts login, "ADMIN" can delete any accounts, other users can only delete their own by specifying the account to delete which is tag to their email. 



## DATABASE:

details of users regardless of user_roles are stored on locally on MySQL.

Mock data

| id | last_login | first_name | last_name | company | user_role  | designation | email             | password                                                                            | is_staff | is_superuser |
|----|------------|------------|-----------|---------|------------|-------------|-------------------|-------------------------------------------------------------------------------------|----------|--------------|
| 24 | NULL       | tester     | testing   |         | ADMIN      |             | trial@test.com    | pbkdf2_sha256$390000$7Q8ISGpuWwHZtVNkG7i5U5$NbiBfEnj0LTGXKiv0KdwWVfvnyA6b97oyPp53XWbeis= | 1        | 1            |
| 25 | NULL       | dan        | teed      |         | TECHNICIAN |             | 1em@em.com        | pbkdf2_sha256$390000$WbtRK6KeSHKLd0F8kVmO0i$r9OUSsnsdgf04sRwPR1R6XyGuMz1FQKHbNIb/wMaBIs= | 1        | 0            |
| 26 | NULL       | dan        | as        |         | ADMIN      |             | 2em2@em.com       | pbkdf2_sha256$390000$oxHeOWna6eo3rTiYL7QgZl$6XipGfuHQue4D1+np3JfWgZ3yF29O6DoBO12DZD3Vyk= | 1        | 1            |
| 27 | NULL       | Shawn      | Thiah     | SMU     | ADMIN      | Intern      | admin@admin.com   | pbkdf2_sha256$390000$wJaepM32doVCy1kVTj1Ue5$MrAR6T7wWQF0zF97Y+B+W/rblPaZAZvTtiaGWTH0Fbk= | 1        | 1            |
