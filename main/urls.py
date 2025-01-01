from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),


    path('detail/<int:pk>/', documentation_detail_view, name='detail'),
    path('get-ip/', get_ip),
]
