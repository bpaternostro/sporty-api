from rest_framework.routers import DefaultRouter
from apps.main.views.language import *

router = DefaultRouter()
router.register(r"languages", LanguageViewSet)
