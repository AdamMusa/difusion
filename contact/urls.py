from django.urls import path
from contact.views import (ContactCreateView, ContactListView,
                            ContactUpdateView,ContactDeleteView,
                            RepertoireDetailView)
from django.views.generic.base import RedirectView

app_name = 'contact'

urlpatterns = [
    path('<int:pk>/', ContactCreateView.as_view(),name='create'),
    path('list/<int:pk>/', ContactListView.as_view(),name='list'),
    path('<int:pk>/contacts/', RepertoireDetailView.as_view(), name='detail'),
    path('create/<int:pk>/', ContactCreateView.as_view(), name='create_contact'),
    path('create/<int:pk>/', ContactUpdateView.as_view(),name='create'),
    path('delete/<int:pk>', ContactDeleteView.as_view(),name='delete'), 
]