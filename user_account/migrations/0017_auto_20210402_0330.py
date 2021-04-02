# Generated by Django 3.1.1 on 2021-04-01 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_account', '0016_filterchoice'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='Confirmed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='Pending',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='Rejected',
            field=models.BooleanField(default=False),
        ),
    ]