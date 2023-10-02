from rest_framework.routers import DefaultRouter
from .views import BookViewSet

router = DefaultRouter()
router.register('catalog', BookViewSet)
urls = router.urls