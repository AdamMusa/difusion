from django.urls import path
from contact.views import (ContactCreateView, ContactListView,
                            ContactUpdateView,ContactDeleteView)
from django.views.generic.base import RedirectView

app_name = 'contact'

urlpatterns = [
    path('', ContactCreateView.as_view(),name='index'),
    path('list/', ContactListView.as_view(),name='list'),
    path('index/<int:pk>/', ContactUpdateView.as_view(),name='index'),
    path('delete/<int:pk>', ContactDeleteView.as_view(),name='delete'), 
]