from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework.views import APIView

from main.serializers import RegisterValidateSerializer

from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from main.signal import IsSuperUser


class RegisterAPIView(APIView):
    def post(self, request):
        User.objects.create_user(
            **request.data
        )
        return Response(data={'message': 'User creadet'})
    def delete(self, request):
        return Response(data={'message': 'OK'})

