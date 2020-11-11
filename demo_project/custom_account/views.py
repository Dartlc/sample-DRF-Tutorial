from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserCredentialsSerializers


# Create your views here.

@api_view(['POST'])
def create_user(request):
    if request.method == 'POST':
        pass
