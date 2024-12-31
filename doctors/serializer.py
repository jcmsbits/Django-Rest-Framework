from rest_framework import serializers
from .models import Doctor, Department, DoctorAvailability, MedicalNote


class DoctorSerializer(serializers.ModelSerializer) :
    class Meta:
        model = Doctor
        fields = "__all__"

    # Si queremos validar solo un campo ponemos validate_nombredelcampo
    def validate_email(self, value):
    # value == "hola@example.com"
        if "@example.com" in value:
                return value
    
        raise serializers.ValidationError("El correo debe incluir @example.com")
    
    # Si queremos validar varios campos usamos validate

    def validate(self, attrs):
        # attrs es un diccionario con todos los campos de los modelos

        if len(attrs['contact_number']) <= 10 and attrs['is_on_vacation'] == True:
            raise serializers.ValidationError(
                "Por favor, ingrese un número válido antes de irte a vacaciones"
            )

        return super().validate(attrs)


class DepartmentSerializer(serializers.ModelSerializer) :
    class Meta:
        model = Department
        fields = "__all__"
    

class DoctorAvailabilitySerializer(serializers.ModelSerializer) :
    class Meta:
        model = DoctorAvailability
        fields = "__all__"

class MedicalNoteSerializer(serializers.ModelSerializer) :
    class Meta:
        model = MedicalNote
        fields = "__all__"
