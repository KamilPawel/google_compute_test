from rest_framework import serializers


class ContactSerializer(serializers.Serializer):
    first_name = serializers.CharField(default="")
    last_name = serializers.CharField(default="")
    email = serializers.CharField()
    phone = serializers.CharField(default="")
    message = serializers.CharField()
