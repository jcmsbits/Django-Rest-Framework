from rest_framework import viewsets
from .serializer import DoctorSerializer
from .models import Doctor
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permissions import IsDoctor

class DoctorViewSet(viewsets.ModelViewSet):
    serializer_class = DoctorSerializer
    queryset = Doctor.objects.all()
    # Primero ponemos IsAuthenticatedOrReadOnly para saber si estamos autenticados o no
    # luego ponemos que averigue si está en el grupo de doctores o no
    permission_classes = [IsAuthenticatedOrReadOnly, IsDoctor]

    # Los endpoints deben ser idempotente
    # Con detail = True específicamos que va a hacer acciones en 1 item
    # Cuando enviemos la url pedira un id
    @action(["POST"], detail = True, url_path= "toggle-on-vacation")
    def toggle_on_vacation(self, request, pk):
        doctor = self.get_object()        
        doctor.is_on_vacation = True
        doctor.save()
        return Response({"status" : "El Doctor está de vacaciones"})
    
    @action(["POST"], detail = True, url_path= "toggle-off-vacation")
    def toggle_off_vacation(self, request, pk):
        doctor = self.get_object()        
        doctor.is_on_vacation = False       
        doctor.save()
        return Response({"status" : "El Doctor no está de vacaciones"})
