from backend.basics.models import City, Gender, Building_Ownership, License_Ownership

from rest_framework import serializers

class CitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = City
        fields = ['name']

class GenderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Gender
        fields = ['name', 'gender']

class BuildingOwnershipSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Building_Ownership
        fields = ['name']

class LicenseOwnershipSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = License_Ownership
        fields = ['name']
