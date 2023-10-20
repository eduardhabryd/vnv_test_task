from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.shortcuts import render
from django.views import generic


class UserListView(generic.ListView):
	model = get_user_model()


class GroupListView(generic.ListView):
	model = Group
