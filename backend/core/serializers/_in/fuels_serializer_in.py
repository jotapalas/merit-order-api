from rest_framework import serializers


class FuelsSerializerIn(serializers.Serializer):
    def __init__(self, *args, **kwargs):
        # Override init method for using parentheses in fields names
        super().__init__(*args, **kwargs)
        self.fields['gas(euro/MWh)'] = serializers.DecimalField(
            max_digits=8, decimal_places=2, required=True
        )
        self.fields['kerosine(euro/MWh)'] = serializers.DecimalField(
            max_digits=8, decimal_places=2, required=True
        )
        self.fields['co2(euro/ton)'] = serializers.DecimalField(
            max_digits=8, decimal_places=2, required=True
        )
        self.fields['wind(%)'] = serializers.IntegerField(
            required=True
        )

    def validate(self, data):
         wind = data.get('wind(%)', 0)
         if wind < 0 or wind > 100:
             raise serializers.ValidationError({'wind': 'wind must be between 0 and 100'})

         return data
