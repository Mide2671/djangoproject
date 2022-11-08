from django.urls import path

from . import views

urlpatterns = [
    path('Home', views.Home, name='Home'),
    path('menu', views.menu, name="menu"),
    path('Register', views.Register, name='Register'),
    path('Sign', views.Sign, name='Sign'),
    path('logout', views.logout),
    path('order', views.order)
]
