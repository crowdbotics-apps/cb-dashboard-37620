from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated


from user_apps.models import UserApp
from user_apps.api.v1.serializers import UserAppSerializer

class UserAppList(APIView):
    serializer_class = UserAppSerializer
    permission_classes = (IsAuthenticated,)

    """
    List all user_apps, or create a new user_app.
    """
    def get(self, request, format=None):
        user_apps = UserApp.objects.filter(user=self.request.user)
        serializer = UserAppSerializer(user_apps, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = UserAppSerializer(data=request.data)
        if serializer.is_valid():
            print(serializer.validated_data)
            serializer.save(user=self.request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserAppDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return UserApp.objects.get(pk=pk, user=self.request.user)
        except UserApp.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        user_app = self.get_object(pk)
        serializer = UserAppSerializer(user_app)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        user_app = self.get_object(pk)
        serializer = UserAppSerializer(user_app, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        user_app = self.get_object(pk)
        user_app.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)