from django.test import TestCase
from core.serializers import PowerPlantSerializerIn


class PowerPlantSerializerInTestCase(TestCase):
    def setUp(self):
        self.powerplant = {
            'name': 'gasfiredbig1',
            'type': 'gasfired',
            'efficiency': 0.53,
            'pmin': 100,
            'pmax': 460
        }

    def test_serializer(self):
        serializer = PowerPlantSerializerIn(data=self.powerplant)
        self.assertTrue(serializer.is_valid())

    def test_invalid_type(self):
        self.powerplant['type'] = 'foo'
        serializer = PowerPlantSerializerIn(data=self.powerplant)
        self.assertFalse(serializer.is_valid())

    def test_invalid_efficiency(self):
        self.powerplant['efficiency'] = 'foo'
        serializer = PowerPlantSerializerIn(data=self.powerplant)
        self.assertFalse(serializer.is_valid())

    def test_invalid_pmin(self):
        self.powerplant['pmin'] = 'foo'
        serializer = PowerPlantSerializerIn(data=self.powerplant)
        self.assertFalse(serializer.is_valid())

    def test_invalid_pmax(self):
        self.powerplant['pmax'] = 'foo'
        serializer = PowerPlantSerializerIn(data=self.powerplant)
        self.assertFalse(serializer.is_valid())
    