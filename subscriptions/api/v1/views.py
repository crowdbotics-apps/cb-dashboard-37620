from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from subscriptions.models import Subscription
from subscriptions.api.v1.serializers import SubscriptionSerializer

class SubscriptionListView(APIView):
    serializer_class = SubscriptionSerializer
    permission_classes = (IsAuthenticated,)

    """
    List all subscription, or create a new user_app.
    """
    def get(self, request, format=None):
        user_subscriptions = Subscription.objects.filter(user=self.request.user)
        serializer = SubscriptionSerializer(user_subscriptions, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SubscriptionSerializer(data=request.data, context={"request": request})
        if serializer.is_valid():
            print(serializer.validated_data)
            serializer.save(user=self.request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 


class SubscriptionDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Subscription.objects.get(pk=pk, user=self.request.user)
        except Subscription.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        user_app = self.get_object(pk)
        serializer = SubscriptionSerializer(user_app)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        user_app = self.get_object(pk)
        serializer = SubscriptionSerializer(user_app, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)