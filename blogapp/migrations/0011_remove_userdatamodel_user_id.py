# Generated by Django 3.1.5 on 2023-08-07 13:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0010_userdatamodel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userdatamodel',
            name='user_id',
        ),
    ]
