from django.urls import path
from rest_framework.routers import DefaultRouter
from .viewsets import DoctorViewSet

router = DefaultRouter()
router.register("doctors", DoctorViewSet)
urlpatterns = [
] + router.urls
