from .blocks import *
from .exercises import *
from .routine_customer_indicator import *
from .routines_blocks_days import *
from .routines_blocks import *
from .routines import *
from .list_values import *

# Create your views here.
def index(request):
    return HttpResponse("<h2>index page</h2>")


def routines(request, id):
    routine = get_list_or_404(
        Routine, id=id
    )  # esto es para encontrar un ID especifico, sino return nada, devuelve un 404
    routines = list(Routine.objects.values())  # trae un listado completo
    return JsonResponse(routines, safe=False)