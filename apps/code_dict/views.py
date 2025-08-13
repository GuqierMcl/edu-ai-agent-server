from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from AAServer import app_properties
from AAServer.common.pagination import CwsPageNumberPagination
from AAServer.response import R, ResponseEnum
from apps.code_dict.models import Code
from apps.code_dict.serializers import CodeSerializer


class CodeView(APIView):
    """
    CodeView handles the code dictionary operations.
    """

    def post(self, request, *args, **kwargs):
        """
        新增码表
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        cs = CodeSerializer(data=request.data)
        cs.is_valid(raise_exception=True)
        cs.save(sequence=cs.validated_data['sequence'] if 'sequence' in cs.validated_data else 1)
        return R.success(cs.validated_data)

    def get(self, request, *args, **kwargs):
        """
        获取码表列表
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        type_name = request.GET.get('type')
        qs = Code.objects.all()
        if type_name:
            qs = qs.filter(type=type_name)
        paginator = CwsPageNumberPagination()
        page = paginator.paginate_queryset(qs, request)
        serializer = CodeSerializer(page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def put(self, request, *args, **kwargs):
        """
        更新码表
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        _id = request.data.get('id')
        if not _id:
            return R.fail(ResponseEnum.PARAM_IS_BLANK, data={'id': 'ID is required'})

        code = Code.objects.get(id=_id)
        serializer = CodeSerializer(code, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()
        return R.success(data=CodeSerializer(instance).data)

    def delete(self, request, *args, **kwargs):
        """
        删除码表
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        _ids = request.GET.getlist('ids')
        if not _ids:
            return R.fail(ResponseEnum.PARAM_IS_BLANK, data={'ids': 'IDs are required'})
        codes = Code.objects.filter(id__in=_ids)
        deleted_count = codes.delete()
        if deleted_count == 0:
            return R.fail(ResponseEnum.PARAM_IS_INVAlID, data={'ids': _ids})
        return R.success(data={'deleted_count': deleted_count})


@api_view(['GET'])
def get_options(request, type_name):
    """
    获取选项列表
    :param type_name:
    :param request:
    :return:
    """
    if not type_name:
        return R.fail(ResponseEnum.PARAM_IS_BLANK)

    codes = Code.objects.filter(type=type_name).values('code', 'name')
    if not codes:
        return R.fail(ResponseEnum.DATA_NOT_FOUND, data={'type': type_name})

    return R.success(data=CodeSerializer(codes, many=True).data)

@api_view(['GET'])
def get_code_type(request):
    """
    获取码表类型
    :param request:
    :return:
    """
    return R.success(app_properties.Code.CODE_TYPE)