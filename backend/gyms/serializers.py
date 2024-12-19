from backend.gyms.models import Gym
from rest_framework import serializers

class GymSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Gym
        fields = ['name', 'city', 'address', 'postal', 'license_number', 'license_start', 'license_expire', 'gender']