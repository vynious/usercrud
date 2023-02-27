from django.db import models
from django.contrib.auth import models as auth_models
from django.contrib.auth.models import PermissionsMixin

# Create your models here.

class UserManager(auth_models.BaseUserManager):

    def create_user(self, email:str, first_name:str, last_name:str, user_role:str, company:str , designation:str, password:str, is_staff=True,is_superuser=False):
        if not email:
            raise ValueError('User must have an Email')
        if not first_name:
            raise ValueError('User must have a First Name')
        if not last_name:
            raise ValueError('User must have a Last Name')
        
        

        user = self.model(
            email = self.normalize_email(email),
            first_name = first_name,
            last_name = last_name,
            company = company,
            designation = designation,
            user_role = user_role,
        )

        if user_role == "ADMIN":
            is_superuser = True
        
        user.is_active=True
        user.is_staff=is_staff
        user.is_superuser=is_superuser
        user.set_password(password)
        user.save()
        return user
    

    def create_superuser(self, email:str, first_name:str, last_name:str, company:str, user_role:str , designation:str, password:str):
      
        user = self.create_user(
            email = email,
            password = password,
            first_name = first_name,
            last_name = last_name,
            company = company,
            designation = designation,
            user_role = user_role,
            is_staff = True,
            is_superuser = True,   
        )
        user.save()
        return user

class User(auth_models.AbstractBaseUser, PermissionsMixin):

    username = None
    first_name = models.CharField(verbose_name='First Name', max_length=100, blank=False)
    last_name = models.CharField(verbose_name='Last Name', max_length=100, blank=False)
    company = models.CharField(verbose_name='Company', max_length=100, blank=True)
    role_level = [
        ('ADMIN','ADMIN'),
        ('MEMBER','MEMBER'),
        ('TECHNICIAN','TECHNICIAN'),
    ]
    user_role = models.CharField(choices=role_level, max_length=100, default='MEMBER')
    designation = models.CharField(verbose_name='Designation', max_length=100, blank=True)
    email = models.EmailField(verbose_name='Email Address', max_length=1000, blank=False, unique=True)
    password = models.CharField(verbose_name='Password', max_length=100)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name','last_name','user_role','company','designation']


  
