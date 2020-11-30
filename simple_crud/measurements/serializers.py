from rest_framework import serializers

from measurements.models import Project, Measurement


class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project


class MeasurementSerializer(serializers.ModelSerializer):

    class Meta:
        model = Measurement
        fields = ('value', 'project')
