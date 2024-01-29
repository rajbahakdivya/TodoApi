from rest_framework.views import APIView
from rest_framework.response import Response

from .serializer import *
from .emails import *

from django.utils import timezone
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken

class RegisterAPI(APIView):

    def post(self, request):
        try:
            data = request.data
            serializer = UserSerializer(data=data)

            if serializer.is_valid():
                serializer.save()
                send_otp_via_email(serializer.data['email'])
                return Response({
                    'status': 200,
                    'message': 'Registration successful, check email',
                    'data': serializer.data,
                })

            return Response({
                'status': 400,
                'message': 'Something went wrong',
                'data': serializer.errors  # Corrected typo: 'error' to 'errors'
            })

        except Exception as e:
            print(e)
            return Response({
                'status': 500,
                'message': 'Internal Server Error',
                'data': None,
            })


class VerifyOTP(APIView):
    def post(self, request):
        try:
            data = request.data
            serializer = VerifyAccountSerializer(data=data)

            if serializer.is_valid():
                email = serializer.validated_data['email']
                otp = serializer.validated_data['otp']

                A = timezone.now()+ timezone.timedelta(minutes=5)
                user = User.objects.get(email=email)
                if user:
                    if user.otp == otp and user.otp_expires_at < timezone.now()+ timezone.timedelta(minutes=5):
                        if user.is_verified:
                                return Response({
                                'status': 400,
                                'message': 'User is already verified',
                                'data': None
                                })
                        user.is_verified = True
                        user.save()

                        return Response({
                            'status': 200,
                            'message': 'Account Verified',
                            'data': None,
                        })
                                
                    return Response({
                        'status': 400,
                        'message': 'Wrong or expired OTP',
                        'data': None
                    })  
                return Response({
                        'status' : 400,
                        'message' : 'Something went wrong',
                        'data' : 'Invalid email'
                    })


                

            return Response({
                'status': 400,
                'message': 'Invalid input data',
                'data': serializer.errors
            })

        except Exception as e:
            print(e)
            return Response({
                'status': 500,
                'message': 'Internal Server Error',
                'data': None,
            })
        

class LoginAPI(APIView):

    def post(self, request):
        try:
            data = request.data
            user= User.objects.filter(email=data['email']).first()
            if user:
                return Response({
                'status': 400,
                'message': 'successfully logged in',
            })

            serializer = LoginSerializer(data=data)
            if serializer.is_valid():
                email = serializer.data['email']
                password = serializer.data['password']
                user = authenticate(request, email=email, password=password)

                if user is None:
                    return Response({
                        'status': 400,
                        'message': 'Invalid credentials',
                        'data': {},
                    })

                if not user.is_verified:
                    return Response({
                        'status': 400,
                        'message': 'Account is not verified',
                        'data': {},
                    })

                

                return Response({
                    'status': 200,
                    'message': 'Login successful',
                    'data': {},
                })

            return Response({
                'status': 400,
                'message': 'Something went wrong',
                'data': serializer.errors,
            })

        except Exception as e:
            print(e)


    def get(self, request):
        return Response({
            'status': 200,
            'message': 'GET request handled',
            'data': {},
        })
        

