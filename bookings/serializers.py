from rest_framework import serializers

from .models import Appointment, MedicalNote

class AppointmentSerializers(serializers.ModelSerializer) :
    
    class Meta : 
        model = Appointment
        fields = "__all__"


class MedicalNoteSerializers(serializers.ModelSerializer) :
    
    class Meta : 
        model = MedicalNote
        fields = "__all__"