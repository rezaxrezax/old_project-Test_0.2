from django.urls import path

from loginsys import views

urlpatterns = [
    path('login/', views.login, name='loginsys'),
    path('logout/', views.logout, name='logoutsys'),
    path('register/', views.register, name='register'),
]