from rest_framework import routers
from polls.viewsets import *

ROUTER = routers.DefaultRouter()
ROUTER.register(r'layout', LayoutViewSet)
ROUTER.register(r'module', ModuleViewSet)
ROUTER.register(r'moduleName', ModuleNameViewSet)