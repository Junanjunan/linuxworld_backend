from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        
        fields = (
            'id',
            'username',
            'password',
        )

        read_only_fields = (
            'id',
        )

    def create(self, validated_data):
        password = validated_data.get("password")
        user = user().create(validated_data)
        user.set_password(password)
        user.save()
        return user