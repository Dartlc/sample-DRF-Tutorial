from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from ..serializers import RegistrationSerializers
from custom_account.serializers import UserCredentialsSerializers
from django.apps import apps


@api_view(['POST'])
def create_user(request):
    if request.method == 'POST':
        serializers = RegistrationSerializers(data=request.data)
        if serializers.is_valid(raise_exception=True):
            serializers.save()
            data = {
                "email": serializers.data['email'],
                'password': serializers.data['password'],
            }
            user_credentials = UserCredentialsSerializers(data=data or None)
            if user_credentials.is_valid(raise_exception=True):
                user_credentials.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_406_NOT_ACCEPTABLE)
    return Response({'error': 'Method Not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['GET'])
def get_all_credentials(request):
    if request.method == 'GET':
        user_credentials = apps.get_model('custom_account', 'UserCredentials')
        records = user_credentials.objects.all()
        print(records)
        if records:
            result = {"success": 'record_found'}
            return Response(result, status=status.HTTP_200_OK)
        else:
            result = {"success": 'No record_found'}
            return Response(result, status=status.HTTP_200_OK)
    return Response({'errors': 'Invalid'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
