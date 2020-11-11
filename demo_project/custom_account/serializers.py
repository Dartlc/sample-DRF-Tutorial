from rest_framework import serializers
from .models import UserCredentials


class UserCredentialsSerializers(serializers.HyperlinkedModelSerializer):
    password = serializers.CharField(max_length=225, min_length=6, write_only=True)

    class Meta:
        model = UserCredentials
        fields = ['email', 'password']

    def validate(self, attrs):
        username = attrs.get('email', '')

        if username is None:
            raise serializers.ValidationError('The username should not be empty')
        return attrs

    def create(self, validated_data):
        return UserCredentials.objects.create_user(**validated_data)
