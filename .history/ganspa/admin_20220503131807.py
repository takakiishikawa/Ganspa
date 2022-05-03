from django.contrib import admin

from .models import Account
admin.site.register(Account)

from .models import Friend
admin.site.register(Friend)

# Register your models here.
