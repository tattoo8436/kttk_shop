# Generated by Django 3.2.18 on 2023-04-16 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('image', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagemodel',
            name='productId',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='imagemodel',
            name='img',
            field=models.FileField(upload_to='images/%Y/%m/%d'),
        ),
    ]
