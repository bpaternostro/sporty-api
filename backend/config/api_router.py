from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from apps.routines.urls import router as routine_router
from apps.customers.urls import router as customer_router
from apps.main.urls import router as core_router
from apps.authentication.urls import router as auth_router
#from apps.core.urls import urlpatterns as core_urls

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.registry.extend(routine_router.registry)
router.registry.extend(customer_router.registry)
router.registry.extend(core_router.registry)
router.registry.extend(auth_router.registry)

app_name = "api"
urlpatterns = router.urls # + core_urls
