from django.urls import path
from . import views
from .models import Loja


urlpatterns = [
    path('', views.index, name='index'),
    path('<int:loja_id>', views.loja, name='loja'),
]
