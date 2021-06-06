import copy

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.permissions import IsAuthenticated

from quizzify.users.permissions import AdminPermission

from .serializers import (
    OrganizationSerializer
)

from .models import (
    Organization
)

class OrganizationListCreateView(APIView):
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

    def get(self, request):
        queryset = Organization.objects.all()
        return Response(
            OrganizationSerializer(queryset, many=True).data,
            status=status.HTTP_200_OK
        )

class OrganizationRetrieveUpdateDelete(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        return Response(
            status=status.HTTP_200_OK
        )