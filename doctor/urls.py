from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .import views

router = DefaultRouter()
router.register('list', views.DoctorViewset)
router.register('designation', views.DesignationViewset)
router.register('availabletime', views.AvailableTimeViewset)
router.register('specialization', views.SpecializationViewset)
router.register('reviews', views.ReviewViewset)

urlpatterns = [
    path('', include(router.urls)),
]