import copy

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.permissions import IsAuthenticated

from quizzify.users.permissions import AdminPermission

from .serializers import (
    OrganizationSerializer
)

class OrganizationCreateView(APIView):
    permission_classes = [IsAuthenticated, AdminPermission]

    def post(self, request):
        data = copy.deepcopy(request.data)

        serializer = OrganizationSerializer(data=data)

        if serializer.is_valid():
            org = serializer.save()
            return Response(
                OrganizationSerializer(org).data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializers.errors,
            status=status.HTTP_400_BAD_REQUEST
        )