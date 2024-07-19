from django.contrib import admin
from .models import Appointment
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
# Register your models here.

class AppointmentAdmin(admin.ModelAdmin):
    list_display=['dfirst_name', 'pfirst_name', 'appointment_types', 'appointment_status', 'symptom', 'time', 'cancel']
    def dfirst_name(self, obj):
        return f'Dr. {obj.doctor.user.first_name}'
    def pfirst_name(self, obj):
        return obj.patient.user.first_name
    def save_model(self, request, obj, form, change):
        obj.save()
        if obj.appointment_status == 3 and obj.appointment_types == 2:
            email_subject = "Your Online Appointment is Running"
            email_body = render_to_string('admin_email.html', {'user' : obj.patient.user, 'doctor' : obj.doctor})
            
            email = EmailMultiAlternatives(email_subject , '', to=[obj.patient.user.email])
            email.attach_alternative(email_body, "text/html")
            email.send()
            # return Response("Check Your Email for Confirmaton.")
admin.site.register(Appointment, AppointmentAdmin)