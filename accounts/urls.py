from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/', views.myLoginView.as_view(), name='login'),
    path('register/', views.register_view, name='register'),
    path('home/', views.HomeView.as_view(), name='home'),
    path('logout/', views.MyLogoutView.as_view(), name='logout'),
]
