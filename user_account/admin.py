from django.contrib import admin
from django.contrib.auth.models import Group

from .models import *

# Register your models here.

admin.site.register(Account)
admin.site.unregister(Account)
admin.site.unregister(Group)
admin.site.site_header="User Account Management"


class Filter(admin.ModelAdmin):
    list_display = ("Name", "Pending", "Confirmed", "Rejected")
    list_filter = ("Pending", "Confirmed", "Rejected")

admin.site.register(User, Filter)




