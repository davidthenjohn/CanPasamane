from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as modelAdmin
from usuari.models import User
from .form import UserChangeForm,UserCreationForm

# Register your models here.
# class UserAdmin(modelAdmin):
#     form = UserChangeForm
#     add_form = UserCreationForm

#     list_display = ("nom_user", "email" , "is_admin")
#     list_filter = ("is_admin",)
#     fieldsets = (
#         (None, {"fields": ("nom_user", "email", "contrasenya", "telefon")}),
#         ("Personal info", {"fields": ("cognoms_user",)}),
#         ("Permissions", {"fields": ("is_admin",)}),
#     )

#     search_fields = ("nom_user",)
#     ordering = ("nom_user",)
#     filter_horizontal = ()

admin.site.register(User)
admin.site.unregister(Group)