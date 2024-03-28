from rest_framework import routers
from .views import ConsumerViewSet

router = routers.SimpleRouter()
router.register(r'consumers', ConsumerViewSet, basename="consumer")
urlpatterns = router.urls
