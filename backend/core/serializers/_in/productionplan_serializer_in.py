from rest_framework import serializers
from .fuels_serializer_in import FuelsSerializerIn
from .powerplant_serializer_in import PowerPlantSerializerIn


class ProductionPlanSerializerIn(serializers.Serializer):
    load = serializers.IntegerField(required=True)
    fuels = FuelsSerializerIn(required=True)
    powerplants = PowerPlantSerializerIn(required=True, many=True)
