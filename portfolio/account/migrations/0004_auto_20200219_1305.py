# Generated by Django 3.0.2 on 2020-02-19 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20200219_0910'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personalinfo',
            name='date_of_birth',
            field=models.DateField(),
        ),
    ]
