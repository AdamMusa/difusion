from django.urls import path
from projet.views import (RepertoireCreateView, RepertoireListView,
                            RepertoireUpdateView,RepertoireDeleteView)
from django.views.generic.base import RedirectView

app_name = 'projet'

urlpatterns = [
    path('', RepertoireCreateView.as_view(),name='index'),
    path('list/', RepertoireListView.as_view(),name='list'),
    path('index/<int:pk>/', RepertoireUpdateView.as_view(),name='index'),
    path('delete/<int:pk>', RepertoireDeleteView.as_view(),name='delete'), 
]