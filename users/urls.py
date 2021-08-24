from django.urls import path
from .import views
from django.contrib.auth import views as auth_view

urlpatterns = [
	path('',views.home),
    
   #path('', auth_views.LoginView.as_view(template_name="home.html"), name="home")

] 