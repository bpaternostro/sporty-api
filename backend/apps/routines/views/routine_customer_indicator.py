from rest_framework.decorators import permission_classes
from rest_framework.response import Response
from rest_framework import viewsets, status
from ...customers import serializers

from ..models import RoutineCustomerIndicator
from ...customers.models import Customer
from ...customers.serializers import CustomerSerializer
from ...authentication.permissions import CustomerAccessPermission

@permission_classes([CustomerAccessPermission])
class RoutineCustomerIndicatorViewSet(viewsets.ModelViewSet):
    queryset = RoutineCustomerIndicator.objects.all()
    serializer_class = serializers.RoutineCustomerIndicatorSerializer

    def create(self, request):
        data = serializers.RoutineCustomerIndicatorSerializer(data=request.data)
        if data.is_valid():
            RoutineCustomerIndicator.objects.create(**data.validated_data)
            customer = Customer.objects.get(id=data.validated_data.get("customer").id)
            return Response(CustomerSerializer(customer).data,
                            status=status.HTTP_201_CREATED)
        else:
            return Response(data.errors,
                            status=status.HTTP_400_BAD_REQUEST)