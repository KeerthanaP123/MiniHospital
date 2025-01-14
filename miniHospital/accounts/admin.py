from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account, demo
from django.utils.html import format_html

# Register your models here.


class AccountAdmin(UserAdmin):
    def thumbnail(self, object):
        if object.usr_img:
            return format_html('<img src="{}" width="100" style="border-radius : 20px;" />'.format(object.usr_img.url))
        else:
            return format_html('<img src="https://res.cloudinary.com/mini-hospital/image/upload/v1663391619/man_vtqh4u.png" width="100" style="border-radius : 20px;" />')

    thumbnail.short_description="Photo"
    list_display = ('thumbnail','email', 'first_name', 'last_name', 'username','state','district','dob','gender', 'last_login', 'date_joined', 'is_active')
    list_display_links = ('email','thumbnail')
    readonly_fields = ('last_login', 'date_joined')
    ordering = ('-date_joined',)
    filter_horizontal = ()
    list_filter = ['email', 'last_login', 'date_joined', 'is_active']
    fieldsets = ()

    
admin.site.register(Account, AccountAdmin)


