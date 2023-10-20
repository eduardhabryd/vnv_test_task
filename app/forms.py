from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from .models import CustomGroup


class UserCreationCustomForm(UserCreationForm):
	email = forms.EmailField(
		required=True,
	)
	
	class Meta(UserCreationForm.Meta):
		model = get_user_model()
		fields = UserCreationForm.Meta.fields + (
			"email",
			"group"
		)


class UserUpdateForm(forms.ModelForm):
	password = forms.CharField(
		label="New Password",
		widget=forms.PasswordInput,
		required=False
	)
	
	confirm_password = forms.CharField(
		label="Confirm Password",
		widget=forms.PasswordInput,
		required=False
	)
	
	class Meta:
		model = get_user_model()
		fields = (
			"email",
			"group",
		)
	
	def clean(self):
		cleaned_data = super().clean()
		password = cleaned_data.get("password")
		confirm_password = cleaned_data.get("confirm_password")
		
		if password or confirm_password:
			if password != confirm_password:
				self.add_error('password', "Passwords do not match")
				self.add_error('confirm_password', "Passwords do not match")
	
	def save(self, commit=True):
		user = super().save(commit=False)
		password = self.cleaned_data.get('password')
		
		if password:
			user.set_password(password)
		
		if commit:
			user.save()
		
		return user

# class DriverCreationForm(UserCreationForm):
#     class Meta(UserCreationForm.Meta):
#         model = Driver
#         fields = UserCreationForm.Meta.fields + (
#             "license_number",
#             "first_name",
#             "last_name",
#         )
#
#     def clean_license_number(self):  # this logic is optional, but possible
#         return validate_license_number(self.cleaned_data["license_number"])


