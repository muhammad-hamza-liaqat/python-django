from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from authapp.serializer import RegisterSerializer, CustomTokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from server.utils import success_response, error_response

class SignupView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return success_response(
                message="User registered successfully",
                data={"id": user.id, "email": user.email},
                status_code=201
            )
        return error_response(
            error="Validation failed",
            details=serializer.errors,
            status_code=400
        )

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer