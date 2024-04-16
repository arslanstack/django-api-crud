from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from account.serializers import UserRegistrationSerializer, UserLoginSerializer, UserProfileSerializer, UserChangePasswordSerializer, SendPasswordResetEmailSerializer, UserPasswordResetSerializer
from django.contrib.auth import authenticate, get_user_model
from account.renderers import UserRenderer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.serializers import ModelSerializer
from rest_framework.permissions import IsAuthenticated


def get_access_token_for_user(user):
    refresh = RefreshToken.for_user(user)
    return str(refresh.access_token)


def get_refresh_token_for_user(user):
    refresh = RefreshToken.for_user(user)
    return str(refresh)


class UserRegistrationView(APIView):
    renderer_classes = [UserRenderer]

    def post(self, request, format=None):
        serializer = UserRegistrationSerializer(data=request.data)
        if (serializer.is_valid(raise_exception=True)):
            serializer.save()
            token = get_access_token_for_user(serializer.instance)
            user = get_user_model().objects.get(email=serializer.instance.email)
            user_serializer = UserProfileSerializer(user)
            user_data = user_serializer.data
            user_data['token'] = token
            user_data['message'] = "User Registered Successfully"
            return Response(user_data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLoginView(APIView):
    renderer_classes = [UserRenderer]

    def post(self, request, format=None):
        serializer = UserLoginSerializer(data=request.data)
        if (serializer.is_valid(raise_exception=True)):
            email = serializer.data.get('email')
            password = serializer.data.get('password')
            user = authenticate(email=email, password=password)
            if user is not None:
                token = get_access_token_for_user(user)
                # get user data from model
                user_serializer = UserProfileSerializer(user)
                user_data = user_serializer.data
                user_data['token'] = token
                return Response(user_data, status=status.HTTP_200_OK)
            else:
                return Response({'errors': {'non_field_errors': ['Incorrect email or password!']}}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserProfileView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        serializer = UserProfileSerializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UserRefreshView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        user_serializer = UserProfileSerializer(request.user)
        user_data = user_serializer.data
        user_data['token'] = get_access_token_for_user(request.user)
        return Response(user_data, status=status.HTTP_200_OK)


class UserChangePasswordView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        serializer = UserChangePasswordSerializer(
            data=request.data, context={'user': request.user})
        serializer.is_valid(raise_exception=True)
        return Response({'msg': 'Password Changed Successfully'}, status=status.HTTP_200_OK)


class SendPasswordResetEmailView(APIView):
    renderer_classes = [UserRenderer]

    def post(self, request, format=None):
        serializer = SendPasswordResetEmailSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response({'msg': 'Password Reset link send. Please check your Email'}, status=status.HTTP_200_OK)


class UserPasswordResetView(APIView):
    renderer_classes = [UserRenderer]

    def post(self, request, uid, token, format=None):
        serializer = UserPasswordResetSerializer(
            data=request.data, context={'uid': uid, 'token': token})
        serializer.is_valid(raise_exception=True)
        return Response({'msg': 'Password Reset Successfully'}, status=status.HTTP_200_OK)
