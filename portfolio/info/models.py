from django.db import models


# Create your models here.

class Skill(models.Model):
    title = models.CharField(max_length=100,unique=True)
    rating = models.IntegerField()

    class Meta:
        db_table = "skill"


class Education(models.Model):
    degree = models.CharField(max_length=100)
    program = models.CharField(max_length=100,unique=True)
    board = models.CharField(max_length=100)
    institution = models.CharField(max_length=100)
    graduation_year = models.DateField()

    class Meta:
        db_table = "education"

class Experience(models.Model):
    title = models.CharField(max_length=20)
    organization = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    job_location = models.CharField(max_length=10)
    work_hour = models.CharField(max_length=20)
    responsibility = models.CharField(max_length=100)
    level = models.CharField(max_length=20)

    class Meta:
        db_table = "experience"

