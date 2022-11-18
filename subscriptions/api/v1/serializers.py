from rest_framework import serializers
from subscriptions.models import Subscription

class SubscriptionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subscription
        fields = '__all__' 

        extra_kwargs = {
            'id': {'read_only': True}, 
            'user': {'read_only': True},
            'created_at': {'read_only': True}, 
            'updated_at': {'read_only': True}, 
            'plan': {
                'required': True,
            },
            'app': {
                'required': True,
            },
            'active': {
                'required': True,
            }}

    def validate_app(self, app):
        current_user = self.context['request'].user

        if app.user != current_user:
            raise serializers.ValidationError("Must be the owner of the app")

        if app.subscription:
            raise serializers.ValidationError("This app already has a subscription associated with it, please make that inactive and try again")