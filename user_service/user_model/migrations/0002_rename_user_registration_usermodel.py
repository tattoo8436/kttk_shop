# Generated by Django 3.2.18 on 2023-05-07 01:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_model', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='user_registration',
            new_name='UserModel',
        ),
    ]
