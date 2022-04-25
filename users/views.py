from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from .forms import *
from django.contrib.auth.models import User
from .models import *
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin
from books.models import Book
from django.http import JsonResponse

# Create your views here.

def registerPage(request):
	if request.user.is_authenticated:
		return redirect('/')
	else:
		form = CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				username = form.cleaned_data.get('username')
				user = User.objects.get(username=username)
				user_profile = Profile.objects.create(user=user)
				user_profile.save()
				messages.success(request, 'Account was created for ' + username)

				return redirect('/login')


		context = {'form':form}
		return render(request, 'register.html', context)

def loginPage(request):
	if request.user.is_authenticated:
		return redirect('/')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('/')
			else:
				messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request, 'login.html', context)

@login_required
def logoutUser(request):
	logout(request)
	return redirect('/')

@login_required
def UserProfileView(request, id):
	if not request.user.is_authenticated:
		return redirect('/login')
	else:
		if request.user.id == id:
			favourites = []
			for book in Book.objects.all():
				if book.is_favourite(request.user.id) == True:
					favourites.append(book)
			context = {'user': request.user,
					   'profile': Profile.objects.get(user=request.user),
					   'favourites': favourites,}
			return render(request, 'user-profile.html', context)
		else:
			return redirect('/')

@login_required
def EditProfileView(request, id):
	if not request.user.is_authenticated:
		return redirect('/login')
	else:
		if request.user.id == id:
			profile = Profile.objects.get(user=request.user)
			if request.method == 'POST':

				user_form = UpdateUserForm(request.POST, instance=request.user)
				profile_form = UpdateProfileForm(request.POST, request.FILES, instance=profile)

				if user_form.is_valid() and profile_form.is_valid():
					user_form.save()
					profile_form.save()
					messages.success(request, 'Your profile is updated successfully')
					return redirect('user-profile', id=request.user.id)
			else:
				user_form = UpdateUserForm(instance=request.user)
				profile_form = UpdateProfileForm(instance=profile)

			return render(request, 'user-profile-edit.html', {'user_form': user_form, 'profile_form': profile_form})

class ChangePasswordView(SuccessMessageMixin, PasswordChangeView):
	template_name = 'change-password.html'
	success_message = "Successfully Changed Your Password"
	success_url = '/logout'


def add_to_reading_list(request, id):
	if request.method == "POST":
		result = ''
		book = get_object_or_404(Book, id=id)
		if book.favourites.filter(id=request.user.id).exists():
			book.favourites.remove(request.user)
			result = 'removed'
			book.save()
		else:
			book.favourites.add(request.user)
			result = 'added'
			book.save()
		return JsonResponse({'result': result, })

