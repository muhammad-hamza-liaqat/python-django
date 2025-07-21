from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from authapp.serializer import RegisterSerializer, CustomTokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from server.utils import success_response, error_response
from rest_framework.response import Response
from rest_framework import status


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

class GetUserView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        # print(f"incoming user------->", user)
        # print(f"incoming user------->", user.name)
        # print(f"incoming user------->", user.id)
        # print(f"incoming user------->", user.gender)
        return Response({
            "status_code": 200,
            "message": "User information fetched successfully",
            "user_information": {
                "id": user.id,
                "name": user.name,
                "email": user.email,
                "phone": user.phone,
                "gender": user.gender,
            }
        }, status=status.HTTP_200_OK)