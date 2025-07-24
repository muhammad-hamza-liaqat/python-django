from rest_framework import serializers
from rest_framework.exceptions import APIException
from authapp.models import User
from django.contrib.auth import authenticate
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['email', 'name', 'phone', 'gender', 'password']

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token["email"] = user.email
        token["name"] = user.name
        token["is_admin"] = user.is_admin
        return token

    def validate(self, attrs):
        email = attrs.get("email")
        password = attrs.get("password")

        try:
            User.objects.get(email=email)
        except User.DoesNotExist:
            raise APIException({
                "status_code": 404,
                "message": "No account found with this email."
            })

        user = authenticate(request=self.context.get("request"), email=email, password=password)
        if user is None:
            raise APIException({
                "status_code": 409,
                "message": "Invalid Password"
            })

        if not user.is_active:
            raise APIException({
                "status_code": 403,
                "message": "User account is inactive."
            })

        refresh = self.get_token(user)

        return {
            "status_code": 200,
            "message": "Login successful",
            "token":{
                'access': str(refresh.access_token),
                'refresh': str(refresh)
                },
                'user': {
                    'id': user.id,
                    'name': user.name,
                    'email': user.email
                }
        }
