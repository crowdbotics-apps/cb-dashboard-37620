from rest_framework.viewsets import ReadOnlyModelViewSet
from .serializers import PlanSerializer
from plans.models import Plan
from rest_framework.permissions import IsAuthenticated


class PlanViewSet(ReadOnlyModelViewSet):
    """
    A simple ViewSet for viewing plans.
    """

    queryset = Plan.objects.all()
    serializer_class = PlanSerializer
    permission_classes = (IsAuthenticated,)
