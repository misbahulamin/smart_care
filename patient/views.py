from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Patient
from . import serializers
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from rest_framework.authtoken.models import Token

# for sending email
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
# Create your views here.
class PatientViewset(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = serializers.PatientSerializers

class RegistrationApiView(APIView):
    serializer_class = serializers.RegistrationSerializers
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token = default_token_generator.make_token(user)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            confirm_link = f'https://smart-care-2.onrender.com/patient/active/{uid}/{token}'
            email_subject = "Confirm your Email - Medical Web"
            email_body = render_to_string('confirm_email.html', {'confirm_link': confirm_link})
            email = EmailMultiAlternatives(email_subject, '', to=[user.email])
            email.attach_alternative(email_body, 'text/html')
            email.send()
            return Response("Check Your Email for Confirmaton.")
        return Response(serializer.errors)
    
def activate(request, uid64, token):
    try:
        uid = urlsafe_base64_decode(uid64).decode()
        user = User.defalut_manager.get(pk=uid)
    except(User.DoesNotExit):
        user = None
    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        return redirect('login')
    else:
        return redirect('register')
    

class LoginApiView(APIView):
    def post(self, request):
        serializer = serializers.LoginSerializers(data = self.request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']

            user = authenticate(username= username, password=password)
            
            if user:
                token, _ = Token.objects.get_or_create(user=user)
                # print(token)
                # print(_)
                login(request, user)
                return Response({'token' : token.key, 'user_id' : user.id})
            else:
                return Response({'error' : "Invalid Credential"})
        return Response(serializer.errors)

class LogoutApiView(APIView):
    def get(self, request):
        request.user.auth_token.delete()
        logout(request)
         # return redirect('login')
        return Response({'success' : "logout successful"})
    
    
    
# {
#     "username": "towaha",
#     "password":"Towaha459@"
# }