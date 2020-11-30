from django.db import models


class Project(models.Model):

    name = models.TextField()
    latitude = models.FloatField()
    longitude = models.FloatField()


class TimestampFields(models.Model):

    class Meta:
        abstract = True

    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )


class Measurement(TimestampFields):

    value = models.FloatField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    image = models.ImageField(blank=True)
