from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models  # --> 같은폴더에있는 models을 import한다


@admin.register(models.User)  # 한칸띄우면 안됨 decorater
class CustomUserAdmin(UserAdmin):  # User를 contraol
    """"Custom User Admin"""

    fieldsets = UserAdmin.fieldsets + (
        (
            "Custom Profile",
            {
                "fields": (
                    "avatar",
                    "gender",
                    "bio",
                    "birthdate",
                    "language",
                    "currency",
                    "superhost",
                )
            },
        ),
    )
    pass


# Register your models here.
