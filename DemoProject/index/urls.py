"""
    Route function paths
"""

from django.urls import path
from .views import *

urlpatterns = [
    path('', sample, name='sample'),
]
