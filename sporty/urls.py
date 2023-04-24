"""sporty URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from routines import views
from django.urls import path
from django.conf.urls import url, include
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r"exercises", views.ExerciseViewSet)
router.register(r"routines", views.RoutineViewSet)
router.register(r"routines-blocks", views.RoutineBlockViewSet)
router.register(r"routines-blocks-days", views.RoutineDaysBlocksViewSet)
router.register(r"blocks", views.BlocksViewSet)
router.register(r"restrictions", views.RestrictionsViewSet)
router.register(r"exercise-type", views.ExerciseTypeViewSet)
router.register(r"muscle-group", views.MuscleGroupViewSet)
router.register(r"routine-types", views.RoutineTypesViewSet)
router.register(r"levels", views.LevelViewSet)
router.register(r"status", views.StatusViewSet)

urlpatterns = [
    url(r"^api/", include(router.urls)),
    path("", views.index),
    # path("exercise", views.exercises),
    path("hello/<str:param>", views.hello),
    path("admin/", admin.site.urls),
    # path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]
