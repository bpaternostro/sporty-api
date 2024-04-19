from django.db.models import Avg
from rest_framework.response import Response
from rest_framework import serializers, status

from ..routines.serializers import RoutineSerializer, RoutineCustomerIndicatorCalculationSerializer
from .models import (
    Customer,
    CustomUser
)
from ..routines.models import Routine, RoutineCustomerIndicator

# Serializers define the API representation.
class CustomerUpdateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Customer
        fields = ["country",
                  "date_of_birth",
                  "weight",
                  "height",
                  "imc",
                  "customer_with_equipement",
                  "customer_train_at_home",
                  "customer_with_lack_space",
                  "customer_with_lack_time",
                  "customer_test_values",
                  "goals", 
                  "level", 
                  "restrictions", 
                  "trainings_preferences"]

class CustomerSerializer(serializers.ModelSerializer):

    routines = serializers.SerializerMethodField()
    height = serializers.SerializerMethodField()
    weight = serializers.SerializerMethodField()
    imc = serializers.SerializerMethodField()
    date_of_birth = serializers.SerializerMethodField()
    kpis = serializers.SerializerMethodField()

    class Meta:
        model = Customer
        fields = ["customer", 
                  "routines",
                  "country",
                  "date_of_birth",
                  "weight",
                  "height",
                  "imc",
                  "customer_with_equipement",
                  "customer_train_at_home",
                  "customer_with_lack_space",
                  "customer_with_lack_time",
                  "customer_test_values",
                  "goals", 
                  "level", 
                  "restrictions", 
                  "trainings_preferences",
                  "kpis"]
        depth = 1


    def get_routines(self, obj):
        routines = Routine.objects.filter(id__in=obj.routines.values_list('id', flat=True))
        return RoutineSerializer(routines, many=True).data
    
    def get_height(self, obj):
        return obj.height if obj.height else 0
    
    def get_weight(self, obj):
        return obj.weight if obj.weight else 0
    
    def get_imc(self, obj):
        return obj.imc if obj.imc else 0
    
    def get_date_of_birth(self, obj):
        return obj.date_of_birth.strftime('%Y-%m-%d') if obj.date_of_birth else ""
    
    def get_kpis(self, obj):
        indicators = RoutineCustomerIndicator.objects.filter(customer=obj.id).all()
        return RoutineCustomerIndicatorCalculationSerializer(indicators).data
    


class RoutineCustomerIndicatorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = RoutineCustomerIndicator
        fields = '__all__'