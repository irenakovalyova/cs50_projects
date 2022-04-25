from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Profile
from djrichtextfield.models import RichTextWidget



class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']



class UpdateUserForm(forms.ModelForm):
	first_name = forms.CharField(max_length=100,
							 required=True,
							 widget=forms.TextInput(attrs={'class': 'user-profile-page-edit-profile-textinput1 input'}))
	last_name = forms.CharField(max_length=100,
							required=True,
							widget=forms.TextInput(attrs={'class': 'user-profile-page-edit-profile-textinput1 input'}))
	username = forms.CharField(max_length=100,
						   required=True,
						   widget=forms.TextInput(attrs={'class': 'user-profile-page-edit-profile-textinput1 input'}))
	email = forms.EmailField(required=True,
						 widget=forms.TextInput(attrs={'class': 'user-profile-page-edit-profile-textinput1 input'}))

	class Meta:
		model = User
		fields = ['first_name', 'last_name', 'username', 'email']


class UpdateProfileForm(forms.ModelForm):
	avatar = forms.ImageField(widget=forms.FileInput(attrs={'class': 'avatar-upload'}))
	bio = forms.CharField(widget=forms.Textarea(attrs={'class': 'user-profile-page-edit-profile-textarea textarea', 'rows': 5}))



	class Meta:
		model = Profile
		fields = ['avatar', 'bio']
