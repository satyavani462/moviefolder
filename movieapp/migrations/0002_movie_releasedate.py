# Generated by Django 3.1 on 2020-09-07 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='releasedate',
            field=models.DateField(null=True),
        ),
    ]
