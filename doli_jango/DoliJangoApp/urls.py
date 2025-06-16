from django.urls import path, include
from DoliJangoApp import views
from .views import (TerceroListView,TerceroCreateView)

urlpatterns = [
    path(r'', views.index, name='index'),
    path(r'index/', views.index, name='index'),
    
    # URLs para Clientes
    path('tercero/', TerceroListView.as_view(), name='tercero-list'),
    path('tercero/nuevo/', TerceroCreateView.as_view(), name='tercero-create'),
]