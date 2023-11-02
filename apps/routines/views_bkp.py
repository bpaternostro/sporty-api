from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_list_or_404

from rest_framework import viewsets, permissions
from .serializers import *

# Create your views here.
def index(request):
    return HttpResponse("<h2>index page</h2>")


def hello(request, username):
    return HttpResponse("<h2>demo %s</h2>" % username)


def routines(request, id):
    routine = get_list_or_404(
        Routine, id=id
    )  # esto es para encontrar un ID especifico, sino return nada, devuelve un 404
    routines = list(Routine.objects.values())  # trae un listado completo
    return JsonResponse(routines, safe=False)