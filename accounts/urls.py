from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),   # code
    path('logout/', views.logout_view, name='logout'), # code
    path('home/', views.home_view, name='home'),      # code
]
