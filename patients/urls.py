from django.urls import path
# from .views import list_patients, detail_patient, ListPatientView
from .views import detail_patient, ListPatientView, DetailPatientView
from rest_framework.routers import DefaultRouter
from .viewsets import PatientViewSet

router = DefaultRouter()
router.register("patients", PatientViewSet) 

# Con el router obtenemos todas las urls de las ViewSet y las quitamos del path
# de urlpatterns y concatenamos el router al final de esta variable
urlpatterns = [
    # path("patients/", list_patients),
    # cuando se le coloca un slash al final de la url se le indica que obtenga 
    # lo que hay entre slash y slash
    # path("patients/<int:pk>/", detail_patient),
    # path("patients/<int:pk>/", DetailPatientView.as_view()),
    # path("patients/", ListPatientView.as_view())
] + router.urls
