from rest_framework import viewsets
from .models import Appointment, MedicalNote
from rest_framework.decorators import action



# class AppointmentsViewsets(viewsets.ModelViewSet):
    
#     @action(["POST", "GET"], detail = True)
#     def appointments(self, request, pk):
#         doctor = 

    
# class MedicalNoteSerializer(viewsets.ModelSerializer):
#     class Meta:
#         model = MedicalNote
#         fields = "__all__"