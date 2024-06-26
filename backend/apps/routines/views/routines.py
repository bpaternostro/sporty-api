from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, get_list_or_404
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator

from rest_framework.decorators import permission_classes

from ..models import Routine
from rest_framework import viewsets
from .. import serializers

from ..models import RoutineCustomers, RoutineDaysBlocks, BlockExerciseDetail, Block
from ...main.models import Language
from ...authentication.permissions import CustomerAccessPermission

@permission_classes([CustomerAccessPermission])
class RoutineViewSet(viewsets.ModelViewSet):
    queryset = Routine.objects.all()
    serializer_class = serializers.RoutineSerializer

    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        #id = self.kwargs['id']
        return Routine.objects.all()
    
    def get_translation(obj, code):
        lang = obj.lang.filter(code=code)

    @method_decorator(cache_page(60*15))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    @action(methods=['get'], detail=False, url_path='export/(?P<pk>[^/.]+)/(?P<lang>[^/.]+)')
    def export(self, request: Request, pk: str = None, lang:str = "es") -> Response:
        routine_customer = get_object_or_404(RoutineCustomers, pk=pk)
        routine = routine_customer.routine
        routine_days_blocks = RoutineDaysBlocks.objects.filter(routine=routine.pk)
        block_exercises_details = [{"day":b.day, "blocks_detail": { block:BlockExerciseDetail.objects.filter(block=block).all() for block in b.blocks.all()}} for b in routine_days_blocks]
        lang = get_object_or_404(Language, code=lang)
        data = {
            "customer": routine_customer.customer,
            "routine": routine,
            "routine_day_blocks": routine_days_blocks,
            "block_exercises_details": block_exercises_details,
            "langs":Language.objects.all(),
            "lang":lang.id,
        }
        return render(request, f'export_template_{lang.code}.html', data)