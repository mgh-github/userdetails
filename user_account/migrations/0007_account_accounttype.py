# Generated by Django 3.1.1 on 2021-04-01 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_account', '0006_user_type_of_account'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='AccountType',
            field=models.CharField(choices=[('EM', 'Employed'), ('UEM', 'Unemployed'), ('ST', 'Student')], default=True, max_length=100),
            preserve_default=False,
        ),
    ]
