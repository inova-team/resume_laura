# Generated by Django 2.2.13 on 2021-09-27 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='bibText',
            field=models.FileField(blank=True, null=True, upload_to='article/bibtext/'),
        ),
    ]
