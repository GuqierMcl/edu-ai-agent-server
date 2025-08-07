from rest_framework.decorators import api_view, authentication_classes, permission_classes

from AAServer.response import R, ResponseEnum
from apps.auth.models import User
from apps.auth.services import do_login


@api_view(['POST'])
@authentication_classes(())
@permission_classes(())
def login(request):
    # 参数校验
    account = request.data['account']
    password = request.data['password']
    if not account or not password:
        return R.fail(ResponseEnum.PARAM_IS_BLANK)

    user = User.objects.get(account=account)
    if not user or not user.check_password(password):
        return R.fail(ResponseEnum.USER_LOGIN_ERROR)

    return R.success(do_login(user, request))



