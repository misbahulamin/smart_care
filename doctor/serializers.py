from rest_framework import serializers
from .models import Doctor, Designation, AvailableTime, Specialization, Review

class DoctorSerializers(serializers.ModelSerializer):
    user = serializers.StringRelatedField(many=False)
    designation = serializers.StringRelatedField(many=True)
    Specialization = serializers.StringRelatedField(many=True)
    AvailableTime = serializers.StringRelatedField(many=True)
    class Meta:
        model = Doctor
        fields = '__all__'
class DesignationSerializers(serializers.ModelSerializer):
    user = serializers.StringRelatedField(many=False)
    class Meta:
        model = Designation
        fields = '__all__'
class AvailableTimeSerializers(serializers.ModelSerializer):
    user = serializers.StringRelatedField(many=False)
    class Meta:
        model = AvailableTime
        fields = '__all__'
class SpecializationSerializers(serializers.ModelSerializer):
    user = serializers.StringRelatedField(many=False)
    class Meta:
        model = Specialization
        fields = '__all__'
class ReviewSerializers(serializers.ModelSerializer):
    user = serializers.StringRelatedField(many=False)
    class Meta:
        model = Review
        fields = '__all__'