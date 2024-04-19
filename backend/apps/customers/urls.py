from rest_framework.routers import DefaultRouter
from apps.customers.views.customers import *

router = DefaultRouter()
router.register(r"customers", CustomerViewSet)
