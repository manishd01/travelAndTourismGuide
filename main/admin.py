from django.contrib import admin
from .models import sign_up_add
# Register your models here.


admin.site.register(sign_up_add)

# class signup_admin(admin.ModelAdmin):

#     list= ['first_name', 'last_name', 'username', 'password', 'confirm_password', 'email', 'mobile_number']

