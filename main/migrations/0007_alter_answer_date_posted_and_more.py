# Generated by Django 4.0 on 2021-12-26 16:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_answer_date_posted_job_internship'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 26, 16, 0, 42, 80989)),
        ),
        migrations.AlterField(
            model_name='internship',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 26, 16, 0, 42, 82020)),
        ),
        migrations.AlterField(
            model_name='job',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 26, 16, 0, 42, 81600)),
        ),
    ]
