from django.shortcuts import render
from rest_framework import viewsets
from .models import Appointment
from . import serializers
# Create your views here.
class AppointmentViewset(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = serializers.AppointmentSerializers