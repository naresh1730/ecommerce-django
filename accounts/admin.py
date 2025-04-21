from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account
# Register your models here.
class AccountAdmin(UserAdmin):
    list_display = ('email','first_name','last_name','username','last_login','date_joined','is_active')
    list_display_links=('email','first_name','last_name')
    readonly_fields=('last_login','date_joined') # for display only
    ordering=('-date_joined',)
    filter_horizontal=() # for password read only
    list_filter=() # for password read only
    fieldsets=() # for password read only
admin.site.register(Account,AccountAdmin)