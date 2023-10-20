from django.contrib import admin
from app.models import CustomUser, CustomGroup

admin.site.register(CustomUser)
admin.site.register(CustomGroup)
