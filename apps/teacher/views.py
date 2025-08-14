from django.db import transaction
from django.db.models import Q
from django.shortcuts import render
from rest_framework.views import APIView

from AAServer.common.pagination import CwsPageNumberPagination
from AAServer.response import R, ResponseEnum
from apps.teacher.models import Teacher
from apps.auth.models import User
from apps.teacher.serializers import TeacherCreateSerializer, TeacherSerializer, TeacherFlatUpdateSerializer


class TeacherMngView(APIView):
    """
    教师管理视图
    """

    @transaction.atomic
    def post(self, request):
        """
        添加教师信息
        """
        serializer = TeacherCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        teacher = serializer.save()
        return R.success({
            'teacher_id': teacher.id,
            'user_id': teacher.user.id,
        })

    def get(self, request):
        """
        分页获取教师信息
        :param request:
        :return:
        """
        keyword = request.GET.get('keyword', '').strip()
        qs = Teacher.objects.all()
        if keyword:
            qs = qs.filter(Q(stu_friendly_name__icontains=keyword) |
                           Q(user__name__icontains=keyword) |
                           Q(user__nickname__icontains=keyword) |
                           Q(user__account__icontains=keyword) |
                           Q(user__phone__icontains=keyword) |
                           Q(user__email__icontains=keyword))
        qs = qs.order_by('-create_time')

        paginator = CwsPageNumberPagination()
        page = paginator.paginate_queryset(qs, request)

        serializer = TeacherSerializer(page, many=True)
        return paginator.get_paginated_response(serializer.data)

    @transaction.atomic
    def delete(self, request):
        """
        删除教师信息（逻辑删除）
        """
        ids = request.GET.getlist('ids')
        if not ids:
            return R.fail(ResponseEnum.PARAM_IS_BLANK)
        qs = Teacher.objects.filter(id__in=ids)
        count = qs.count()

        # 获取用户ID列表
        user_ids = qs.values_list('user_id', flat=True).distinct()

        if count == 0:
            return R.fail(ResponseEnum.PARAM_IS_BLANK)
        deleted_count = qs.delete()  # 逻辑删除

        # 删除用户信息
        User.objects.filter(id__in=user_ids).delete()

        return R.success({
            'deleted_count': deleted_count
        })

    @transaction.atomic
    def put(self, request):
        """
        更新教师信息
        :param request:
        :return:
        """
        teacher = Teacher.objects.get(id=request.data.get('id'))
        serializer = TeacherFlatUpdateSerializer(
            instance=teacher,
            data=request.data,
            partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return R.success()
