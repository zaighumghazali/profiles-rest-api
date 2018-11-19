from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class HelloApiView(APIView):
    """Test Api View."""
    def get(self,request, format=None):
        """Returns a list of APIView feature."""
        an_apiview = [
            'Uses HTTP methods as function(get, post, patch, put, delete)',
            'It is similar to a traditional Django view',
            'Gives you the most control over your logic',
            'Its mapped manually to URLs'
        ]

        return Response({'message': 'Hello!' , 'an_apiview' : an_apiview })
