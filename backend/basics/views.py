from backend.basics.models import City, Gender, Building_Ownership, License_Ownership
from rest_framework import permissions, viewsets

from backend.basics.serializers import CitySerializer, GenderSerializer, BuildingOwnershipSerializer, \
    LicenseOwnershipSerializer

class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all().order_by('name')
    serializer_class = CitySerializer
    permission_classes = [permissions.AllowAny]

class GenderViewSet(viewsets.ModelViewSet):
    queryset = Gender.objects.all().order_by('name')
    serializer_class = GenderSerializer
    permission_classes = [permissions.AllowAny]

class BuildingOwnershipViewSet(viewsets.ModelViewSet):
    queryset = Building_Ownership.objects.all().order_by('name')
    serializer_class = BuildingOwnershipSerializer
    permission_classes = [permissions.AllowAny]

class LicenseOwnershipViewSet(viewsets.ModelViewSet):
    queryset = License_Ownership.objects.all().order_by('name')
    serializer_class = LicenseOwnershipSerializer
    permission_classes = [permissions.AllowAny]
