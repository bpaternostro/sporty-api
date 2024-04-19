from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import RegisterView, LoginView, UserView, LogoutView

router = DefaultRouter()
router.register(r"register", RegisterView)
router.register(r"login", LoginView)
router.register(r"user", UserView)
router.register(r"logout", LogoutView)