from rest_framework.viewsets import ModelViewSet
from . import models, serializer

class ProjectsViewSet(ModelViewSet):
  queryset = models.Project.objects.all()
  serializer_class = serializer.ProjectSerializer