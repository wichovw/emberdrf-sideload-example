from rest_framework import viewsets

from example.models import *
from example.serializers import *

class ChildThingViewSet(viewsets.ModelViewSet):
    queryset = ChildThing.objects.all()
    serializer_class = ChildThingSideloadSerializer