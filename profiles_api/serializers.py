from rest_framework import serializers


class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing our APIView"""

    # Serializers also takes care of validtion rules, it will help you validate the data input
    name = serializers.CharField(max_length=10)
