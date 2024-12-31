from datetime import date, time
from rest_framework import serializers
from .models import Patient, Insurance, MedicalRecord
from bookings.serializers import AppointmentSerializers

class PatientSerializers(serializers.ModelSerializer) :
    # Serializers anidados
    # Ponemos read_only igual True porque si alguien manda un post
    # a este endopoint no lo vamos a tomar en cuenta
    
    # La manera en la que los serializadores buscando los campos es
    # primero buscan en la clase(PatientSerializers), luego buscan en 
    # el modelo (model = Patient) y si no lo encuentran muestran un error
    appointments = AppointmentSerializers(many = True, read_only = True)
    
    # Si queremos hacer como un middleware (modificar la información antes de entregarla)
    # Agregamos la variable y le asignamos serializer.SerializerMethodField
    # Sino le pasamos una función como parámetros entonces usa una por defecto
    # que se llama get_"nombre_del_campo"
    age = serializers.SerializerMethodField()

    class Meta :
        model = Patient
        # fields = "__all__"
        fields = [
            "id",
            "first_name",
            "last_name",
            # Agregamos age en los campos
            'age',
            "date_of_birth",
            "contact_number",
            "email",
            "address",
            "medical_history",
            "appointments"
        ]
    
    # 
    def get_age(self, obj):
        
        # date nos devuelve un time delta y tenemos que dividir 365 que son los
        # días que tenemos en el año
        age = date.today() - obj.date_of_birth
        years  = age.days // 365
        return f'{years} años'
        



class InsuranceSerializers(serializers.ModelSerializer) :
    class Meta :
        model = Insurance
        fields = "__all__"


class MedicalRecordSerializers(serializers.ModelSerializer) :
    class Meta :
        model = MedicalRecord
        fields = "__all__"
