from django.db import models
from datetime import date, datetime
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class ChucVu(models.Model):
    Name = models.CharField(max_length=100,null=True)


class Employess(models.Model):
    First_name = models.CharField(max_length=30, null=False)
    Last_name = models.CharField(max_length=30, null=False)
    Phone = models.IntegerField()
    Address = models.CharField(max_length=100)
    Date_of_birth = models.DateField(default=date.today)

    chuc_vu = models.ForeignKey(
        ChucVu, on_delete=models.CASCADE, related_name='nhan_viens')
    user = models.OneToOneField(
        'User', on_delete=models.SET_NULL, null=True, unique=True)

    def getdate(self):
        formatted_date = self.Date_of_birth.strftime('%B %d, %Y')
        date_obj = datetime.strptime(formatted_date, '%B %d, %Y')
        formatted_date = date_obj.strftime('%Y-%m-%d')
        return formatted_date


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """
        Creates and saves a superuser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if not extra_fields.get('is_staff'):
            raise ValueError('Superuser must have is_staff=True.')
        if not extra_fields.get('is_superuser'):
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, max_length=254)
    is_active = models.BooleanField(default=True)
    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'isAdmin', 'address']

    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.name

    def get_short_name(self):
        return self.name.split()[0]
