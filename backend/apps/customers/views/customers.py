from django.http import HttpResponse, JsonResponse
from django.conf import settings
from django.shortcuts import get_list_or_404, get_object_or_404
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator

from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import permission_classes
from rest_framework import status
from rest_framework import viewsets, permissions
from ..serializers import *

from ...authentication.permissions import CustomerAccessPermission

@permission_classes([CustomerAccessPermission])
class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    def get_serializer_class(self):
        serializers = {
            'update_customer_data':  CustomerUpdateSerializer,
        }
        return serializers.get(self.action, CustomerSerializer)
    
    @method_decorator(cache_page(settings.CACHE_TIMEOUT))
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    
    @action(methods=['put'], detail=False, url_path='update/(?P<pk>[^/.]+)')
    def update_customer_data(self, request: Request, pk: str = None) -> Response:
        instance = self.get_object()  # Retrieve the customer instance
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        updated_customer = serializer.save()  # Save the updated instance
        return Response(CustomerSerializer(updated_customer).data, status=status.HTTP_200_OK)
