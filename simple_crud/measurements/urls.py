from django.urls import path

from measurements.views import TestView, MeasurementViewSet, ProjectViewSet
from rest_framework.routers import SimpleRouter


router = SimpleRouter()
router.register('measurements', MeasurementViewSet, basename='measure')
router.register('projects', ProjectViewSet, basename='project')


urlpatterns = [
    path('test/', TestView.as_view(), name='test')
] + router.urls
