from django.urls import path
from .views import home, connecte, deconecte, profile, reset_password,signup, update_password
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', connecte, name='login'),
    path('logout/', deconecte, name='logout'),
    path('signup/', signup, name='signin'),
    path('', home, name='home'),
    path('profile/', profile, name='profile'),
    path('reset-password/', reset_password, name='reset-password'),
    path('update-password/<str:token>/', update_password, name='update-password'),
    
]
