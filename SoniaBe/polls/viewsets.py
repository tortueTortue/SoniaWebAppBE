from rest_framework import viewsets
from .models import *
from .serializers import *

class LayoutViewSet(viewsets.ModelViewSet):
    queryset = Layout.objects.all()
    serializer_class = LayoutSerializer

class ModuleViewSet(viewsets.ModelViewSet):
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer

class ModuleNameViewSet(viewsets.ModelViewSet):
    queryset = ModuleName.objects.all()
    serializer_class = ModuleNameSerializer