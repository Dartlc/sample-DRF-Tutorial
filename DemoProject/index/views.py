"""
    Index Routes
"""
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def sample(request) -> Response:
    """
        Index Program
    :param request: None
    :return: string
    """

    return Response({'data': 'Hello World'}, status=status.HTTP_200_OK)
