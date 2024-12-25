from django.urls import path
# from .views import list_patients, detail_patient, ListPatientView
from .views import detail_patient, ListPatientView, DetailPatientView

urlpatterns = [
    # path("patients/", list_patients),
    # cuando se le coloca un slash al final de la url se le indica que obtenga 
    # lo que hay entre slash y slash
    # path("patients/<int:pk>/", detail_patient),
    path("patients/<int:pk>/", DetailPatientView.as_view()),
    path("patients/", ListPatientView.as_view())
]
