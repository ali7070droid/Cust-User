from django.urls import path
from . import views

urlpatterns = [
	path('', views.start, name='home'),
	path('register/', views.registration_view, name='register')

]