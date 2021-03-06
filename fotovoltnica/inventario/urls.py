from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('register', views.register, name='register'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('systems', views.systems, name='systems'),
    path('cotizar', views.cotizar, name='cotizar'),
    path('contacto', views.contacto, name='contacto'),
]
