# Generated by Django 4.1.7 on 2023-05-11 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_email',
            field=models.CharField(default='', max_length=50),
        ),
    ]
