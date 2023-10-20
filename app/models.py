from django.contrib.auth.models import AbstractUser, Group
from django.db import models


class CustomGroup(Group):
	description = models.TextField(blank=True)
	
	class Meta:
		verbose_name = 'Custom Group'
		verbose_name_plural = 'Custom Groups'


class CustomUser(models.Model):
	username = models.CharField(
		max_length=30,
		unique=True
	)
	group = models.ForeignKey(
		CustomGroup, blank=True, related_name="users", null=True, on_delete=models.PROTECT
	)
	created = models.DateTimeField(auto_now_add=True)


