from django.db import models
from patient.models import Patient
from doctor.models import Doctor, AvailableTime

# Create your models here.
APPOINMENT_STATUS=[
    (1, 'Completed'),
    (2, 'Pending'),
    (3, 'Running'),
    
]
APPOINMENT_TYPES=[
    (1, 'Offline'),
    (2, 'Online'),
    
]
class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    appointment_types = models.IntegerField(choices=APPOINMENT_TYPES)
    appointment_status = models.IntegerField(choices=APPOINMENT_STATUS, default=2)
    symptom = models.TextField()
    time = models.ForeignKey(AvailableTime, on_delete=models.CASCADE)
    cancel = models.BooleanField(default=False)
    
    def __str__(self):
        return f'Doctor: {self.doctor.user.first_name} {self.doctor.user.last_name}; Patient: {self.patient.user.first_name} {self.patient.user.last_name}'
    