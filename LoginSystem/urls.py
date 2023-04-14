from django.urls import path

from LoginSystem import views

urlpatterns=[
    path('',views.home,name='home'),
    path('login',views.login_fun,name='login'),
    path('readlogin',views.login_read,name='readlogin'),
    path('register',views.register_fun,name='register'),
    path('readregister',views.register_read,name='readregister'),
    path('logout',views.logout_fun,name='logout')
]