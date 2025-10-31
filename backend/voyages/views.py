from rest_framework import viewsets
from .models import Voyage
from .serializers import VoyageSerializer

class VoyageViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A simple ViewSet for viewing the voyages.
    We use ReadOnlyModelViewSet because we only want to read the data (GET requests),
    not create or delete it via the API.
    """
    queryset = Voyage.objects.all().order_by('date')
    serializer_class = VoyageSerializer

