from rest_framework import serializers
from .models import Patient, Insurance, MedicalRecord

class PatientSerializers(serializers.ModelSerializer) :
    class Meta :
        model = Patient
        fields = "__all__"

class InsuranceSerializers(serializers.ModelSerializer) :
    class Meta :
        model = Insurance
        fields = "__all__"


class MedicalRecordSerializers(serializers.ModelSerializer) :
    class Meta :
        model = MedicalRecord
        fields = "__all__"
