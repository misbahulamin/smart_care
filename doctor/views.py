from django.shortcuts import render
from rest_framework import viewsets
from .models import Doctor, Designation, AvailableTime, Specialization, Review
from . import serializers
from rest_framework import filters, pagination
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class DesignationViewset(viewsets.ModelViewSet):
    queryset = Designation.objects.all()
    serializer_class = serializers.DesignationSerializers

class AvailableTimeForSpecificDoctor(filters.BaseFilterBackend):
    def filter_queryset(self, request, query_set, view):
        doctor_id = request.query_params.get("doctor_id")
        if doctor_id:
            return query_set.filter(doctor=doctor_id)
        return query_set

class AvailableTimeViewset(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    queryset = AvailableTime.objects.all()
    serializer_class = serializers.AvailableTimeSerializers
    filter_backends = [AvailableTimeForSpecificDoctor]
class SpecializationViewset(viewsets.ModelViewSet):
    queryset = Specialization.objects.all()
    serializer_class = serializers.SpecializationSerializers
class ReviewViewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Review.objects.all()
    serializer_class = serializers.ReviewSerializers
    

class DoctorPagination(pagination.PageNumberPagination):
    page_size = 1 # Total items per page
    page_size_query_param = page_size
    max_page_size = 100

class DoctorViewset(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = serializers.DoctorSerializers
    filter_backends = [filters.SearchFilter]
    pagination_class = DoctorPagination
    search_fields = ['user__first_name', 'user__email', 'designation__name', 'specialization__name']
    
