from rest_framework import routers
from polls.viewsets import LayoutViewSet

router = routers.DefaultRouter()
router.register(r'layout', LayoutViewSet)