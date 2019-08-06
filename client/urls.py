from django.urls import path
from client.views import register,login, logout_view

app_name = 'client'

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('logout/', logout_view, name="logout")
]
