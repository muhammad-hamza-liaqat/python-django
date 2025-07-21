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
                data={"id": user.id, "email": user.email, "user_wallet": user.wallet.id},
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
        wallet = user.wallet
        # print(f"incoming user------->", user)
        # print(f"incoming user------->", user.name)
        # print(f"incoming user------->", user.id)
        # print(f"incoming user------->", user.gender)
        print(f"incoming user------->", user.wallet)
        return Response({
            "status_code": 200,
            "message": "User information fetched successfully",
            "user_information": {
                "id": user.id,
                "name": user.name,
                "email": user.email,
                "phone": user.phone,
                "gender": user.gender,
            },
            "wallet":{
                "wallet_id": str(wallet.id) if wallet else None,
                "balance": str(wallet.balance) if wallet else None,
                "created_at": wallet.created_at.isoformat() if wallet else None
            }
        }, status=status.HTTP_200_OK)