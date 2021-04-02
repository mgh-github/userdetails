# Generated by Django 3.1.1 on 2021-04-01 17:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_account', '0005_remove_user_type_of_account'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='type_of_account',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user_account.account'),
        ),
    ]