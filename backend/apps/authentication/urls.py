from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import RegisterView, LoginView, UserView, LogoutView

router = DefaultRouter()
router.register(r"register", RegisterView, "register")
router.register(r"login", LoginView, "login")
router.register(r"user", UserView, "user")
router.register(r"logout", LogoutView, "logout")