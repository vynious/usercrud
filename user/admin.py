from django.contrib import admin
from . import models

# Register your models here.

class _UserAdmin(admin.ModelAdmin):
    list_display=(
        'id',
        'first_name',
        'last_name',
        'email',
        'designation',
        'company',
        'user_role',
    )


admin.site.register(models.User,_UserAdmin)

