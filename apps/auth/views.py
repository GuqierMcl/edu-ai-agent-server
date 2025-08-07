from django.contrib.auth.hashers import MD5PasswordHasher
from rest_framework.decorators import api_view, authentication_classes, permission_classes

from AAServer.response import R, ResponseEnum
from apps.auth.models import User
from apps.auth.serializers import LoginSerializer
from apps.auth.services import do_login


@api_view(['POST'])
@authentication_classes(())
@permission_classes(())
def login(request):
    # 参数校验
    param = LoginSerializer(data=request.data)
    if not param.is_valid(raise_exception=False):
        return R.fail(ResponseEnum.PARAM_IS_BLANK)


    user = User.objects.get(account=param.data['account'])
    if not user:
        return R.fail(ResponseEnum.USER_NOT_EXIST)

    hasher = MD5PasswordHasher()
    pwd = hasher.encode(param.data['password'], user.password)
    if pwd != user.password:
        R.fail(ResponseEnum.USER_LOGIN_ERROR)

    return R.success(do_login(user, request))



