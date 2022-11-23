from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status as http_status
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema
from rest_framework.exceptions import ValidationError

from subscriptions.models import Subscription
from subscriptions.api.v1.serializers import SubscriptionSerializer


class SubscriptionListView(APIView):
    serializer_class = SubscriptionSerializer
    permission_classes = (IsAuthenticated,)

    """
    List all subscription, or create a new user_app.
    """

    @swagger_auto_schema(responses={http_status.HTTP_200_OK: SubscriptionSerializer(many=True)})
    def get(self, request, format=None):
        user_subscriptions = Subscription.objects.filter(user=self.request.user)
        serializer = SubscriptionSerializer(user_subscriptions, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=SubscriptionSerializer(many=False),
                         responses={http_status.HTTP_201_CREATED: SubscriptionSerializer(many=False),
                                    http_status.HTTP_400_BAD_REQUEST: 'Bad request'})
    def post(self, request, format=None):
        current_user = self.request.user
        serializer = SubscriptionSerializer(data=request.data)
        if serializer.is_valid():
            target_app = serializer.validated_data.get('app')
            # Validate if the current user is the owner of the app.
            if target_app.user != current_user:
                raise ValidationError('Must be the owner of the app')

            if Subscription.objects.filter(user=current_user, app=target_app, active=True).first():
                raise ValidationError(
                    'This app already has a subscription associated with it, please make that inactive and try again')

            serializer.save(user=current_user)
            return Response(serializer.data, status=http_status.HTTP_201_CREATED)
        return Response(serializer.errors, status=http_status.HTTP_400_BAD_REQUEST)


class SubscriptionDetail(APIView):
    serializer_class = SubscriptionSerializer
    permission_classes = (IsAuthenticated,)

    """
    Retrieve, update or delete a snippet instance.
    """

    def get_object(self, pk):
        try:
            return Subscription.objects.get(pk=pk, user=self.request.user)
        except Subscription.DoesNotExist:
            raise Http404

    @swagger_auto_schema(responses={http_status.HTTP_200_OK: SubscriptionSerializer(many=False),
                                    http_status.HTTP_404_NOT_FOUND: 'Subscription not found'})
    def get(self, request, pk, format=None):
        subscription = self.get_object(pk)
        serializer = SubscriptionSerializer(subscription)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=SubscriptionSerializer(many=False),
                         responses={http_status.HTTP_200_OK: SubscriptionSerializer(many=False),
                                    http_status.HTTP_400_BAD_REQUEST: 'Bad request'})
    def put(self, request, pk, format=None):
        current_user = self.request.user
        subscription = self.get_object(pk)
        serializer = SubscriptionSerializer(subscription, data=request.data)

        if serializer.is_valid():
            # Validate if the current user is the owner of the app.
            target_app = serializer.validated_data.get('app')
            if target_app.user != current_user:
                raise ValidationError("Must be the owner of the app")

            if subscription.app.id != target_app.id and Subscription.objects.filter(user=current_user, app=target_app,
                                                                                    active=True).first():
                raise ValidationError(
                    'This app already has a subscription associated with it, please make that inactive and try again')
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=http_status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(request_body=SubscriptionSerializer(many=False),
                         responses={http_status.HTTP_200_OK: SubscriptionSerializer(many=False),
                                    http_status.HTTP_400_BAD_REQUEST: 'Bad request'})
    def patch(self, request, pk, format=None):
        return self.put(self, request, pk, format)
