from django.urls import path
from .views import get_info, get_soccers, detail



urlpatterns = [
    path('', get_info, name='get_info'),
    path('soccer/<int:pk>', get_soccers, name='get_soccer'),
    path('soccer/detail/<int:pk>', detail, name='detail')
]