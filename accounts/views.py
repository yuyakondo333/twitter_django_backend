from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import CustomRegisterSerializer


class UserRegistrationView(APIView):
    def post(self, request):
        serializer = CustomRegisterSerializer(data=request.data)
        if serializer.is_valid():
            try:
                serializer.save()
            except Exception:
                return Response(
                    {"error": "Something went wrong..."},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )
            return Response({
                "message": "ユーザーの作成に成功しました。"
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
