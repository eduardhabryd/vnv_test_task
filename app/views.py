from django.urls import reverse_lazy
from django.views import generic

from .models import CustomGroup, CustomUser


class UserListView(generic.ListView):
	model = CustomUser


class UserCreateView(generic.CreateView):
	model = CustomUser
	fields = "__all__"
	success_url = reverse_lazy("app:user-list")


class UserUpdateView(generic.UpdateView):
	model = CustomUser
	fields = "__all__"
	success_url = reverse_lazy("app:user-list")


class UserDeleteView(generic.DeleteView):
	model = CustomUser
	success_url = reverse_lazy("app:user-list")


class GroupListView(generic.ListView):
	model = CustomGroup


class GroupCreateView(generic.CreateView):
	model = CustomGroup
	success_url = reverse_lazy("app:group-list")
	fields = (
		"name", "description",
	)


class GroupUpdateView(generic.UpdateView):
	model = CustomGroup
	success_url = reverse_lazy("app:group-list")
	fields = (
		"name", "description",
	)


class GroupDeleteView(generic.DeleteView):
	model = CustomGroup
	success_url = reverse_lazy("app:group-list")
