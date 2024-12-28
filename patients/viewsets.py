from rest_framework import viewsets 
from .serializers import PatientSerializers
from .models import Patient

class PatientViewSet(viewsets.ModelViewSet):
    serializer_class = PatientSerializers
    queryset = Patient.objects.all()
