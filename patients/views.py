from .serializers import PatientSerializers
from .models import Patient
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView

# GET /api/patients => Listar
# POST /api/patients => Crear
# PUT /api/patients/<int:pk>/ => Modificación o Actualización
# DELETE /api/patients/<pk>/ => Borrar

"""
{
    "id" : 5,
    "first_name" : "Michael",
    "last_name" : "Williams",
    "date_of_birth" : "1988-07-30",
    "contact_number" : "555-456-7890",
    "email" : "michael.williams@example.com",
    "address" : "202 Birch St, Springfield, USA",
    "medical_history" : "Asthma, treated with inhalers."
}

{
    "id" : 5,
    "first_name" : "Jose Carlos",
    "last_name" : "Machado",
    "date_of_birth" : "1989-10-31",
    "contact_number" : "53-58362592",
    "email" : "jose@example.com",
    "address" : "Alguna en Cuba",
    "medical_history" : "Sin problemas medicos"
}

"""
# Para reducir el código podemos usar clases genericas ya implementadas en Django

# class ListPatientView(APIView) :
class ListPatientView(CreateAPIView, ListAPIView) :
    """
    Obtiene la lista de citas médicas pogramadas    
    """
    allowed_methods = ["GET", "POST"]
    # serializer_class = PatientSerializers

    def get(self, request):
        patients = Patient.objects.all()
        serializer = PatientSerializers(patients, many = True)
        return Response(serializer.data)

    def post(self, request) :
        serializer = PatientSerializers(data = request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        return Response(status = status.HTTP_201_CREATED)


# @api_view(["GET", "POST"])
# def list_patients(request):
    
#     if request.method == "GET":
#         patients = Patient.objects.all()
#         serializer = PatientSerializers(patients, many = True)
#         return Response(serializer.data)

#     if request.method == "POST":
#         serializer = PatientSerializers(data = request.data)

#         # Con raise_exception capturamos y enviamos el error y nos ahorra el if porque no ejecuta
#         # el código que le sigue
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(status=status.HTTP_201_CREATED)

# El problema con este tipo de clases (APIView) es que repetimos mucho código 
class DetailPatientView(RetrieveUpdateDestroyAPIView):
    allowed_methods = ["GET", "PUT", "DELETE"]
    serializer_class = PatientSerializers
    queryset = Patient.objects.all()

    # def get(self, request, pk):

    #     try :
    #         patient = Patient.objects.get(id = pk)

    #     except Patient.DoesNotExist:
    #         return Response(status = status.HTTP_404_NOT_FOUND)
    
    #     serializer = PatientSerializers(patient)
    #     return Response(serializer.data)

    # def put(self, request, pk):
    #     try :
    #         patient = Patient.objects.get(id = pk)

    #     except Patient.DoesNotExist:
    #         return Response(status = status.HTTP_404_NOT_FOUND)
    
    #     serializer = PatientSerializers(patient, data = request.data)
    #     serializer.is_valid(raise_exception = True)
    #     serializer.save()
    #     return Response(serializer.data, status = status.HTTP_201_CREATED)
    
    # def delete(self, request, pk):
        # try :
        #     patient = Patient.objects.get(id = pk)

        # except Patient.DoesNotExist:
        #     return Response(status = status.HTTP_404_NOT_FOUND)
        
        # patient.delete()
        # return Response(status = status.HTTP_204_NO_CONTENT)



@api_view(["GET", "PUT", "DELETE"])
def detail_patient(request, pk):
    try :
        patient = Patient.objects.get(id = pk)

    except Patient.DoesNotExist:

        return Response(status = status.HTTP_404_NOT_FOUND)
        
    if request.method == "GET":
        serializer = PatientSerializers(patient)
        return Response(serializer.data)
    
    if request.method == "PUT":
        serializer = PatientSerializers(patient, data = request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        return Response(serializer.data, status = status.HTTP_201_CREATED)

    if request.method == "DELETE" :
        patient.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
    


class ListPatientView(ListAPIView, CreateAPIView):
    allowed_methods = ["GET", "POST"]
    serializer_class = PatientSerializers
    queryset = Patient.objects.all()