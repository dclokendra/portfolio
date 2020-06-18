from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager
)


# Create your models here.

class AccountManager(BaseUserManager):
    def create_user(self, email, name=None, password=None):
        if not email:
            raise ValueError("User must have email address")
        user = self.model(
            email=self.normalize_email(email),
            name=name,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name=None, password=None):
        user = self.create_user(email, name, password)
        user.is_admin = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):
    email = models.EmailField(
        verbose_name="Enter Your Email",
        unique=True
    )
    name = models.CharField(verbose_name="Full Name", max_length=100, null=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=True)
    objects = AccountManager()
    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email

    def has_perm(self, perm, onj=None):
        return True

    def has_module_perms(self, app_lable):
        return True

    @property
    def is_staff(self):
        return self.is_admin


class PersonalInfo(models.Model):
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    nationality = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    religion = models.CharField(max_length=20)
    photo = models.ImageField(upload_to='info/')
    date_of_birth = models.DateField()

    class Meta:
        db_table = "personal_info"
