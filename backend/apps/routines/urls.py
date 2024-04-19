from rest_framework.routers import DefaultRouter
from apps.routines.views import *

router = DefaultRouter()
router.register(r"exercises", ExerciseViewSet)
router.register(r'routines', RoutineViewSet, 'routines')
router.register(r"routines-blocks", RoutineBlockViewSet)
router.register(r"routines-customer-indicator", RoutineCustomerIndicatorViewSet)
router.register(r"routines-blocks-days", RoutineDaysBlocksViewSet)
router.register(r"blocks", BlocksViewSet)
router.register(r"list-values", ListValuesViewSet, 'list-values')