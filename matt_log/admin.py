from django.contrib import admin

# Register your models here.

from .models import User, Matt, Log_data

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass

@admin.register(Matt)
class MattAdmin(admin.ModelAdmin):
    pass

@admin.register(Log_data)
class Log_dataAdmin(admin.ModelAdmin):
    pass



