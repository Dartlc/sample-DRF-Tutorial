from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from ..serializers import RegistrationSerializers


@api_view(['POST'])
def create_user(request):
    if request.method == 'POST':
        serializers = RegistrationSerializers(data=request.data)
        if serializers.is_valid(raise_exception=True):
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_406_NOT_ACCEPTABLE)
    return Response({'error': 'Method Not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
