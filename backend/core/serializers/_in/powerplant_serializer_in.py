from rest_framework import serializers


class PowerPlantSerializerIn(serializers.Serializer):
    name = serializers.CharField(
        required=True
    )
    type = serializers.ChoiceField(
        choices=['gasfired', 'turbojet', 'windturbine'],
        required=True
    )
    efficiency = serializers.DecimalField(
        max_digits=3, decimal_places=2, required=True
    )
    pmin = serializers.IntegerField(
        required=True
    )
    pmax = serializers.IntegerField(
        required=True
    )
