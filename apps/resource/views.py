import django.conf
from rest_framework.decorators import api_view

from AAServer.common.middleware import GlobalRequestMiddleware
from AAServer.response import R, ResponseEnum
from AAServer.utils.session_utils import SessionUtils
from apps.resource.serializers import ResourceSerializer

# Create your views here.

ENDPOINT = django.conf.settings.MINIO_ENDPOINT
USE_HTTPS = django.conf.settings.MINIO_USE_HTTPS


@api_view(['POST'])
def upload_resource(request):
    """
    上传或获取资源
    :param request:
    :return:
    """
    # 处理上传资源的逻辑
    # 这里可以使用ResourceSerializer来序列化上传的数据
    rs = ResourceSerializer(data=request.data)
    if rs.is_valid():
        file = rs.validated_data['file']  # 2025-8-12/3489700_20250616190501_1_TdFsQoq.png
        rs.save(size=file.size if file else None,
                old_filename=str(file),
                sequence=rs.validated_data['sequence'] if 'sequence' in rs.validated_data else 0)
        return R.success(data=rs.data)
    return R.fail(ResponseEnum.UPLOAD_FAIL, data=rs.errors)
