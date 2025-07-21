from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import SignupView, CustomTokenObtainPairView, GetUserView

urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', CustomTokenObtainPairView.as_view(), name='custom_token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # user routes
    path('user/information/', GetUserView.as_view(), name="get_user_information")
]
