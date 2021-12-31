# Generated by Django 4.0 on 2021-12-26 15:59

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('main', '0005_auto_20211226_1827'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 26, 15, 59, 15, 648092)),
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=500)),
                ('position', models.TextField()),
                ('link', models.URLField(null=True)),
                ('date_posted', models.DateTimeField(default=datetime.datetime(2021, 12, 26, 15, 59, 15, 648842))),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
        ),
        migrations.CreateModel(
            name='Internship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=500)),
                ('position', models.TextField()),
                ('appln_form', models.URLField(null=True)),
                ('date_posted', models.DateTimeField(default=datetime.datetime(2021, 12, 26, 15, 59, 15, 649352))),
                ('duration', models.CharField(max_length=20)),
                ('batches_allowed', models.CharField(max_length=50)),
                ('stipend', models.CharField(max_length=50)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
        ),
    ]
