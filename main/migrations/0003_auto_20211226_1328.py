# Generated by Django 3.1.2 on 2021-12-26 07:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20211226_1325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 26, 13, 28, 5, 565817)),
        ),
        migrations.AlterField(
            model_name='answer',
            name='image',
            field=models.ImageField(upload_to='mainapp/question_images/'),
        ),
        migrations.AlterField(
            model_name='question',
            name='image',
            field=models.ImageField(null=True, upload_to='mainapp/question_images/'),
        ),
    ]
