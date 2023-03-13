from rest_framework import serializers





class JobSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=150)
    age = serializers.CharField(max_length=50)
    url = serializers.CharField(max_length=150)
    description = serializers.CharField(max_length=500)

