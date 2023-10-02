from rest_framework.routers import DefaultRouter
from .views import ShelfViewSet

router = DefaultRouter()
router.register('library-map', ShelfViewSet)
urls = router.urls