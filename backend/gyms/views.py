from django.shortcuts import render
from backend.gyms.models import Gym
from rest_framework import permissions, viewsets

from backend.gyms.serializers import GymSerializer

class GymViewSet(viewsets.ModelViewSet):
    queryset = Gym.objects.all().order_by('license_expire')
    serializer_class = GymSerializer
    permission_classes = [permissions.IsAuthenticated]
