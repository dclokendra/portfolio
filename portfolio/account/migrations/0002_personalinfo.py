# Generated by Django 3.0.2 on 2020-02-18 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonalInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=100)),
                ('nationality', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=10)),
                ('religion', models.CharField(max_length=20)),
                ('photo', models.ImageField(upload_to='info/')),
                ('email', models.EmailField(max_length=254)),
                ('date_of_birth', models.DateField()),
            ],
            options={
                'db_table': 'personal_info',
            },
        ),
    ]
