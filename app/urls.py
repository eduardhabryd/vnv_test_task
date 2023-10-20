from django.contrib import admin
from django.urls import path

from .views import UserListView, UserCreateView, UserUpdateView, GroupListView

urlpatterns = [
    path("users/", UserListView.as_view(), name="user-list"),
    path("users/create/", UserCreateView.as_view(), name="user-create"),
    path("users/<int:pk>/", UserUpdateView.as_view(), name="user-update"),
    path("groups/", GroupListView.as_view(), name="group-list"),
]

app_name = "app"
