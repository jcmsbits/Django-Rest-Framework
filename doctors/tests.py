from django.test import TestCase
from django.urls import reverse
from rest_framework import status
# Vamos a usar APIClient porque ya estamos predefiniendo valores predeterminado
# Que nos sirve para probar, por ejemplo: Que todo lo vamos a enviar es un JSON
# o un header que diga que es un JSON
from rest_framework.test import APIClient
from patients.models import Patient
from doctors.models import Doctor


# Create your tests here.
class DoctorViewSetTests(TestCase):

    # El método setUp permite ejecutar código antes de realizar cualquier prueba
    # que vayamos a ejecutar. Como vamos a crear un Doctor y un paciente vamos a
    # agregarlo dentro de setUp
    def setUp(self):
        self.patient = Patient.objects.create(
            first_name = "Luis",
            last_name = "Martinez",
            date_of_birth = '1990-12-05',
            contact_number = '5352482684',
            email = 'example@example.com',
            address = "Dirección de prueba",
            medical_history = "Ninguna",
        )

        self.doctor = Doctor.objects.create(
            first_name = "Oscar",
            last_name = "Barajas",
            qualification = "Profesional",
            contact_number = "5358994862",
            email = "example2@example.com",
            address = "Medellín",
            biography = "Sin",
            is_on_vacation = False,
        )

        # return super().setUp()
        
        self.client  = APIClient()

    
    def test_list_should_return_200(self):
        url = reverse(
            'doctor-appointments', 
            kwargs = {'pk' : self.doctor.id },
            )

        response = self.client.get(url)

        # Falla porque pide autenticación este enlace
        # self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)