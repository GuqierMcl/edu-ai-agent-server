from django.core.cache import cache
from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework.decorators import api_view

from AAServer.common.cache import cache_get, cache_set
from AAServer.response import R, ResponseEnum
from AAServer.utils.redis_utils import CacheKeys
from apps.auth.models import User
from apps.user.serializers import UserSerializer, UserInfoSerializer


@api_view(['GET'])
def get_user_info(request):
    """
    获取用户信息
    :param request: 请求对象
    :return: 用户信息
    """
    cache_key = CacheKeys.USER_INFO + str(request.user.id)
    user_dict = cache_get(cache_key)
    if not user_dict:
        user_dict = UserSerializer(instance=User.objects.get(id=request.user.id)).data
        cache_set(cache_key, user_dict)
    info = UserInfoSerializer(user_dict)
    return R.success(info.data)