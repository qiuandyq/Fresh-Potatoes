# Generated by Django 3.1.6 on 2021-03-10 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_profile_movies'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='movies',
            field=models.TextField(default='', max_length=1000),
        ),
    ]
