from django.test import TestCase
from core.serializers import FuelsSerializerIn


class FuelsSerializerInTestCase(TestCase):
    def setUp(self):
        self.fuels = {
            'gas(euro/MWh)': 13.4,
            'kerosine(euro/MWh)': 50.8,
            'co2(euro/ton)': 20,
            'wind(%)': 60
        }
    
    def test_serializer(self):
        serializer = FuelsSerializerIn(data=self.fuels)
        self.assertTrue(serializer.is_valid())

    def test_invalid_gas(self):
        self.fuels['gas(euro/MWh)'] = 'foo'
        serializer = FuelsSerializerIn(data=self.fuels)
        self.assertFalse(serializer.is_valid())

    def test_invalid_kerosine(self):
        self.fuels['kerosine(euro/MWh)'] = 'foo'
        serializer = FuelsSerializerIn(data=self.fuels)
        self.assertFalse(serializer.is_valid())

    def test_invalid_c02(self):
        self.fuels['co2(euro/ton)'] = 'foo'
        serializer = FuelsSerializerIn(data=self.fuels)
        self.assertFalse(serializer.is_valid())

    def test_invalid_wind(self):
        self.fuels['wind(%)'] = 'foo'
        serializer = FuelsSerializerIn(data=self.fuels)
        self.assertFalse(serializer.is_valid())

    def test_decimal_wind(self):
        self.fuels['wind(%)'] = 50.4
        serializer = FuelsSerializerIn(data=self.fuels)
        self.assertFalse(serializer.is_valid())

    def test_negative_wind(self):
        self.fuels['wind(%)'] = -2
        serializer = FuelsSerializerIn(data=self.fuels)
        self.assertFalse(serializer.is_valid())

    def test_wind_greater_than_100(self):
        self.fuels['wind(%)'] = 120
        serializer = FuelsSerializerIn(data=self.fuels)
        self.assertFalse(serializer.is_valid())
