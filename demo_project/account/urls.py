from django.urls import path
from .views import index, create_user, get_all_credentials

urlpatterns = [
    path('', index, name='index'),
    path('create/', create_user, name='create'),
    path('details/', get_all_credentials, name='details'),
]
