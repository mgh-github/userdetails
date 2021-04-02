# Generated by Django 3.1.1 on 2021-04-01 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_account', '0017_auto_20210402_0330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='AccountType',
            field=models.CharField(choices=[('EMPLOYED', 'EMP'), ('UNEMPLOYED', 'UNEMP'), ('STUDENT', 'STD')], default='', max_length=100, unique=True),
        ),
    ]