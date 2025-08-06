from django.contrib.auth import authenticate
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from AAServer.response import R
from authentication.models import SysUser


@api_view(['POST'])
@permission_classes((AllowAny,))
def login(request):
    return R.success()
        

