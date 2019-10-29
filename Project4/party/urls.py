from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_party_data, name='get_party_data'),
    path('results', views.display_party_data, name='display_party_data')
]