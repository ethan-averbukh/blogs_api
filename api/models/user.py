from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager



class UserManager(BaseUserManager):
    #Overriding default Django behavior with email instead of username
    #Setting password default to None for validation purposes
    #If no password is passed an error is thrown
    #**extra_fields: For all other extra arguments needed

    def create_user(self, email, password=None, **extra_fields):
        #Custom validation error
        if not email:
            raise ValueError('User must input an email address')
        user_password = password
        user = self.model(email=self.normalize_email(email), **extra_fields)

        #Attempting to encrypt the password with make_password using user input
        user.set_password(password)

        user.save()
        
        return user

    def create_superuser(self,email, password):
        user = self.create_user(email,password)

        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user


class User(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'

    objects = UserManager()

    def __str__(self):
        return self.email