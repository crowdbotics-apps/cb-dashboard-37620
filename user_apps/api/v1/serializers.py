from user_apps.models import UserApp
from rest_framework import serializers

class UserAppSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserApp
        fields = '__all__' 

        extra_kwargs = {
            'user': {'read_only': True}, 
            'id': {'read_only': True}, 
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