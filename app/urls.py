from django.contrib import admin
from django.urls import path

from .views import UserListView, GroupListView

urlpatterns = [
    path("users/", UserListView.as_view(), name="user-list"),
    # path("users/create/", admin.site.urls),
    path("groups/", GroupListView.as_view(), name="group-list"),
]

app_name = "app"
