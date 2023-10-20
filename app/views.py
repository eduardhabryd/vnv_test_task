from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from .forms import UserCreationCustomForm, UserUpdateForm
from .models import CustomGroup


class UserListView(generic.ListView):
	model = get_user_model()


class UserCreateView(generic.CreateView):
	model = get_user_model()
	form_class = UserCreationCustomForm
	success_url = reverse_lazy("app:user-list")


class UserUpdateView(generic.UpdateView):
	model = get_user_model()
	form_class = UserUpdateForm
	success_url = reverse_lazy("app:user-list")


class GroupListView(generic.ListView):
	model = CustomGroup



# class ManufacturerCreateView(LoginRequiredMixin, generic.CreateView):
#     model = Manufacturer
#     fields = "__all__"
#     success_url = reverse_lazy("taxi:manufacturer-list")
#
#
# class ManufacturerUpdateView(LoginRequiredMixin, generic.UpdateView):
#     model = Manufacturer
#     fields = "__all__"
#     success_url = reverse_lazy("taxi:manufacturer-list")
#
#
# class ManufacturerDeleteView(LoginRequiredMixin, generic.DeleteView):
#     model = Manufacturer
#     success_url = reverse_lazy("taxi:manufacturer-list")