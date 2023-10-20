from django.contrib.auth.models import AbstractUser, Group
from django.db import models


class CustomGroup(Group):
	description = models.TextField(blank=True)
	
	class Meta:
		verbose_name = 'Custom Group'
		verbose_name_plural = 'Custom Groups'


class User(AbstractUser):
	groups = models.ManyToManyField(
		CustomGroup, blank=True, related_name="users"
	)


