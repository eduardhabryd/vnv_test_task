from django.contrib.auth.models import AbstractUser, Group
from django.db import models


class CustomGroup(Group):
	data_analytics = models.BooleanField(default=False)
	services_analytics = models.BooleanField(default=False)
	voice_analytics = models.BooleanField(default=False)
	queue_stats = models.BooleanField(default=False)
	voice_stats = models.BooleanField(default=False)
	video = models.BooleanField(default=False)
	smart_access = models.BooleanField(default=False)
	diagrams = models.BooleanField(default=False)
	
	class Meta:
		verbose_name = 'Custom Group'
		verbose_name_plural = 'Custom Groups'


class User(AbstractUser):
	group = models.ForeignKey(
		CustomGroup, blank=True, related_name="users", null=True, on_delete=models.SET_NULL
	)


