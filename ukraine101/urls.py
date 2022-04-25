"""mybookclub URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from pages.views import *
from users.views import *
from books.views import books_list_view, book_details_view
from django.conf import settings
from django.conf.urls.static import static
from users.views import ChangePasswordView, add_to_reading_list


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('support/', support_view, name='support'),
    path('random-fact/', fact_view, name='random-fact'),
    path('books/', books_list_view, name='books-list'),
    path('books/<slug:slug>/', book_details_view, name='book-details'),
    path('fav/<int:id>/', add_to_reading_list, name='reading_list_add'),
    path('articles/', include('articles.urls')),
    path('register/', registerPage, name="register"),
	path('login/', loginPage, name="login"),
	path('logout/', logoutUser, name="logout"),
    path('password-change/', ChangePasswordView.as_view(), name='password_change'),
    path('users/<int:id>/', UserProfileView, name='user-profile'),
    path('users/<int:id>/edit/', EditProfileView, name='edit-user-profile'),
    path('djrichtextfield/', include('djrichtextfield.urls')),
]





if settings.DEBUG:  # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
