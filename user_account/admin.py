from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Account)

class Filter(admin.ModelAdmin):
    list_display = ("Name", "Pending", "Confirmed", "Rejected")
    list_filter = ("Pending", "Confirmed", "Rejected")

admin.site.register(User, Filter)




