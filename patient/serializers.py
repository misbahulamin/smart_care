from rest_framework import serializers
from .models import Patient
from django.contrib.auth.models import User
class PatientSerializers(serializers.ModelSerializer):
    user = serializers.StringRelatedField(many=False)
    class Meta:
        model = Patient
        fields = '__all__'
        
        
class RegistrationSerializers(serializers.ModelSerializer):
    confirm_password = serializers.CharField(required=True)
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'confirm_password']
    
    def save(self):
        username= self.validated_data['username']
        first_name= self.validated_data['first_name']
        last_name= self.validated_data['last_name']
        email= self.validated_data['email']
        password= self.validated_data['password']
        confirm_password= self.validated_data['confirm_password']
        
        if password!=confirm_password:
            raise serializers.ValidationError({'error':'Password does not matched.'})
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({'error':'Email alrady exists.'})
        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError({'error':'User name alrady exists.'})
        account = User(username=username, email=email,first_name=first_name, last_name=last_name,)
        account.set_password(password)
        account.is_active = False
        account.save()
        return account
    
class LoginSerializers(serializers.Serializer):
     username = serializers.CharField(required=True)
     password = serializers.CharField(required=True)