from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status as http_status
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema

from user_apps.models import UserApp
from user_apps.api.v1.serializers import UserAppSerializer


class UserAppList(APIView):
    serializer_class = UserAppSerializer
    permission_classes = (IsAuthenticated,)

    """
    List all user_apps, or create a new user_app.
    """

    @swagger_auto_schema(responses={http_status.HTTP_200_OK: UserAppSerializer(many=True)})
    def get(self, request, format=None):
        user_apps = UserApp.objects.filter(user=self.request.user)
        serializer = UserAppSerializer(user_apps, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=UserAppSerializer(many=False),
                         responses={http_status.HTTP_201_CREATED: UserAppSerializer(many=False),
                                    http_status.HTTP_400_BAD_REQUEST: "Bad request"})
    def post(self, request, format=None):
        serializer = UserAppSerializer(data=request.data)
        if serializer.is_valid():
            print(serializer.validated_data)
            serializer.save(user=self.request.user)
            return Response(serializer.data, status=http_status.HTTP_201_CREATED)
        return Response(serializer.errors, status=http_status.HTTP_400_BAD_REQUEST)


class UserAppDetail(APIView):
    serializer_class = UserAppSerializer
    permission_classes = (IsAuthenticated,)

    """
    Retrieve, update or delete a snippet instance.
    """

    def get_object(self, pk):
        try:
            return UserApp.objects.get(pk=pk, user=self.request.user)
        except UserApp.DoesNotExist:
            raise Http404

    @swagger_auto_schema(responses={http_status.HTTP_200_OK: UserAppSerializer(many=False),
                                    http_status.HTTP_404_NOT_FOUND: "App not found"})
    def get(self, request, pk, format=None):
        user_app = self.get_object(pk)
        serializer = UserAppSerializer(user_app)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=UserAppSerializer(many=False),
                         responses={http_status.HTTP_200_OK: UserAppSerializer(many=False),
                                    http_status.HTTP_400_BAD_REQUEST: "Bad request"})
    def put(self, request, pk, format=None):
        user_app = self.get_object(pk)
        serializer = UserAppSerializer(user_app, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=http_status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(request_body=UserAppSerializer(many=False),
                         responses={http_status.HTTP_200_OK: UserAppSerializer(many=False),
                                    http_status.HTTP_400_BAD_REQUEST: "Bad request"})
    def patch(self, request, pk, format=None):
        return self.put(self, request, pk, format)

    @swagger_auto_schema(responses={http_status.HTTP_204_NO_CONTENT: ""})
    def delete(self, request, pk, format=None):
        user_app = self.get_object(pk)
        user_app.delete()
        return Response(status=http_status.HTTP_204_NO_CONTENT)
