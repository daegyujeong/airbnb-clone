from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models  # --> 같은폴더에있는 models을 import한다
from rooms import models as room_model

# Create your models here.
class RoomInline(admin.TabularInline):

    model = room_model.Room


@admin.register(models.User)  # 한칸띄우면 안됨 decorater
class CustomUserAdmin(UserAdmin):  # User를 contraol
    """"Custom User Admin"""

    inlines = (RoomInline,)
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

    list_filter = UserAdmin.list_filter + ("superhost",)

    list_display = (
        "username",
        "first_name",
        "last_name",
        "email",
        "is_active",
        "language",
        "currency",
        "superhost",
        "is_staff",
        "is_superuser",
    )

    pass


# Register your models here.
