from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import check_password
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import ParseError, NotFound
from rest_framework.permissions import IsAuthenticated
from users.models import User
from .serializers import UserSerializer


class ProfileView(APIView):
    def get(self, request, pk):
        user = User.objects.get(pk=pk)
        serializer = UserSerializer(
            user, 
            context={"request":request}
        ).data
        return Response(serializer)

    def post(self, request, pk):
        password = request.data["password"]
        user = User.objects.get(pk=pk)
        if check_password(password, user.password):     # https://ssungkang.tistory.com/entry/DjangoUser-%EB%B9%84%EB%B0%80%EB%B2%88%ED%98%B8-%EB%B3%80%EA%B2%BD%ED%95%98%EA%B8%B0-checkpassword
            new_password = request.data["new_password"]
            user.set_password(new_password)
            user.save()
        else:
            print("오류오류")
        return Response()


class SignUpView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            new_user = serializer.save()
            new_user.set_password(request.data["password"])
            new_user.save()
            return Response(UserSerializer(new_user).data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LogInView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        if not username or not password:
            raise ParseError
        user = authenticate(
            request,
            username=username,
            password=password,
        )
        if user:
            login(request, user)
            return Response({"ok": "Welcome!"})
        else:
            return Response({"error": "wrong password"})



class LogOutView(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request):
        logout(request)
        return Response({"ok": "bye!"})