from user_apps.models import UserApp
from rest_framework import serializers
from subscriptions.models import Subscription

class UserAppSerializer(serializers.ModelSerializer):

    subscription = serializers.SerializerMethodField()


    def get_subscription(self, obj):
        active_subscription = Subscription.objects.filter(user=obj.user, app=obj).first()
        if active_subscription:
            return active_subscription.id
        else:
            return None

    class Meta:
        model = UserApp
        fields = '__all__' 

        extra_kwargs = {
            'user': {'read_only': True}, 
            'id': {'read_only': True}, 
            'created_at': {'read_only': True}, 
            'updated_at': {'read_only': True}, 
            'name': {
                'required': True,
                'allow_blank': False,
            },
            'type': {
                'required': True,
                'allow_blank': False, 
            },
            'framework': {
                'required': True,
                'allow_blank': False, 
            }}