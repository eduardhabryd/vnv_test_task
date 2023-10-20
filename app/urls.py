from django.urls import path

from .views import (
    UserListView,
    UserCreateView,
    UserUpdateView,
    UserDeleteView,
    GroupListView,
    GroupCreateView,
    GroupUpdateView,
    GroupDeleteView,
)

urlpatterns = [
    path("users/", UserListView.as_view(), name="user-list"),
    path("users/create/", UserCreateView.as_view(), name="user-create"),
    path(
        "users/<int:pk>/update/", UserUpdateView.as_view(), name="user-update"
    ),
    path(
        "users/<int:pk>/delete", UserDeleteView.as_view(), name="user-delete"
    ),
    path("groups/", GroupListView.as_view(), name="group-list"),
    path("groups/create/", GroupCreateView.as_view(), name="group-create"),
    path(
        "groups/<int:pk>/update/",
        GroupUpdateView.as_view(),
        name="group-update",
    ),
    path(
        "groups/<int:pk>/delete/",
        GroupDeleteView.as_view(),
        name="group-delete",
    ),
]

app_name = "app"
