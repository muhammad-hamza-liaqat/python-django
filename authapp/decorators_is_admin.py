from functools import wraps
from rest_framework.response import Response
from rest_framework import status

def admin_required(view_func):
    @wraps(view_func)
    def _wrapped_view(self, request, *args, **kwargs):
        user = request.user

        if not user or not user.is_authenticated:
            return Response({'error': 'Authentication required'}, status=status.HTTP_401_UNAUTHORIZED)

        if not getattr(user, 'is_admin', False):
            return Response({'error': 'Admin access required'}, status=status.HTTP_403_FORBIDDEN)

        return view_func(self, request, *args, **kwargs)

    return _wrapped_view
