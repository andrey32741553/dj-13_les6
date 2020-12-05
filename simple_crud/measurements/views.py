from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from measurements.models import Project, Measurement
from measurements.serializers import ProjectSerializer, MeasurementSerializer


class TestView(APIView):
    def get(self, request, *args, **kwargs):
        return Response({'status': 'ok'})

    def post(self, request, *args, **kwargs):
        print('create something')
        return Response({'status': 'ok'})


class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class MeasurementViewSet(ModelViewSet):
    queryset = Measurement.objects.select_related('project').all()
    serializer_class = MeasurementSerializer
