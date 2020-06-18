from django.db import models


# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    message = models.TextField()
    status = models.BooleanField(default=False)

    class Meta:
        db_table = "contact"
