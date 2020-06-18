# Generated by Django 3.0.2 on 2020-02-19 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('degree', models.CharField(max_length=100)),
                ('program', models.CharField(max_length=100, unique=True)),
                ('board', models.CharField(max_length=100)),
                ('institution', models.CharField(max_length=100)),
                ('graduation_year', models.DateField()),
            ],
            options={
                'db_table': 'education',
            },
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('organization', models.CharField(max_length=100)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('job_location', models.CharField(max_length=10)),
                ('work_hour', models.CharField(max_length=20)),
                ('responsibility', models.CharField(max_length=100)),
                ('level', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'experience',
            },
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True)),
                ('rating', models.IntegerField()),
            ],
            options={
                'db_table': 'skill',
            },
        ),
    ]