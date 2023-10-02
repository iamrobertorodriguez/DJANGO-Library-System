from rest_framework.routers import DefaultRouter
from .views import InvoiceViewSet

router = DefaultRouter()
router.register('invoices', InvoiceViewSet)
urls = router.urls