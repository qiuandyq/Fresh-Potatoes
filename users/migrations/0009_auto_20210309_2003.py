# Generated by Django 3.1.6 on 2021-03-10 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20210309_2001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='movies',
            field=models.CharField(default='', max_length=1000),
        ),
    ]
