from django.db import models
from django.contrib.auth.models import User

class Account(models.Model):
    Account_Type_Choice = [
        ('EMPLOYED', 'EMP'),
        ('UNEMPLOYED', 'UNEMP'),
        ('STUDENT', 'STD')
    ]
    AccountType = models.CharField(max_length=100,unique=True, choices=Account_Type_Choice, default='')

    def __str__(self):
        return self.AccountType


class User(models.Model):
    Name = models.CharField(max_length=200)
    Phone = models.CharField(max_length=12)
    Email = models.EmailField(max_length=200)
    Photo = models.ImageField(upload_to ="uploads/", blank=True)
    type_of_account = models.ForeignKey(Account,to_field='AccountType', on_delete=models.CASCADE)
    Pending = models.BooleanField(default=False)
    Confirmed = models.BooleanField(default=False)
    Rejected = models.BooleanField(default=False)


    def __str__(self):
        return self.Name


class FilterChoice(models.Model):
    Pending = models.BooleanField(default=False)
    Confirmed = models.BooleanField(default=False)
    Rejected = models.BooleanField(default=False)

    def __str__(self):
        return self.Pending
