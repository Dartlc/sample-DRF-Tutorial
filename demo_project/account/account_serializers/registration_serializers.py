from rest_framework import serializers
from ..models import Registration


class RegistrationSerializers(serializers.HyperlinkedModelSerializer):
    last_name = serializers.CharField(required=False, max_length=255, allow_null=True, allow_blank=True)
    address = serializers.JSONField(required=False, allow_null=True)
    qualification = serializers.JSONField(required=False, allow_null=True)

    class Meta:
        model = Registration
        fields = ['first_name', 'last_name', 'email', 'password', 'address', 'qualification']

    def validate(self, attrs):
        first_name = attrs.get('first_name', '')

        if first_name is not None:
            return attrs
