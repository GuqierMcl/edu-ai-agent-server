from django.contrib.auth import authenticate
from rest_framework.decorators import api_view

#
# @api_view
# def login(request):
#     user = authenticate(username=request.data.get('username'), password=request.data.get('password'))