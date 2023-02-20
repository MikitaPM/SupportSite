from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .models import User
from .serializer import UserRegistrSerializer


class RegistrUserView(CreateAPIView):
    queryset = User.object.all()
    serializer_class = UserRegistrSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = UserRegistrSerializer(data = request.data)
        data = {}
        if serializer.is_valid:
            serializer.save
            data['respons'] = True

            return Response(data, status=status.HTTP_200_OK)

        else:
            data =serializer.errors

            return Response(data)

