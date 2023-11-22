from django.test import TestCase
from core.serializers import ProductionPlanSerializerIn


class ProductionPlanSerializerInTestCase(TestCase):
    def setUp(self):
        self.productionplan = {
            "load": 910,
            "fuels":
            {
                "gas(euro/MWh)": 13.4,
                "kerosine(euro/MWh)": 50.8,
                "co2(euro/ton)": 20,
                "wind(%)": 60
            },
            "powerplants": [
                {
                "name": "gasfiredbig1",
                "type": "gasfired",
                "efficiency": 0.53,
                "pmin": 100,
                "pmax": 460
                },
                {
                "name": "gasfiredbig2",
                "type": "gasfired",
                "efficiency": 0.53,
                "pmin": 100,
                "pmax": 460
                },
                {
                "name": "gasfiredsomewhatsmaller",
                "type": "gasfired",
                "efficiency": 0.37,
                "pmin": 40,
                "pmax": 210
                },
                {
                "name": "tj1",
                "type": "turbojet",
                "efficiency": 0.3,
                "pmin": 0,
                "pmax": 16
                },
                {
                "name": "windpark1",
                "type": "windturbine",
                "efficiency": 1,
                "pmin": 0,
                "pmax": 150
                },
                {
                "name": "windpark2",
                "type": "windturbine",
                "efficiency": 1,
                "pmin": 0,
                "pmax": 36
                }
            ]
        }

    def test_serializer(self):
        serializer = ProductionPlanSerializerIn(data=self.productionplan)
        self.assertTrue(serializer.is_valid())

    def test_invalid_load(self):
        self.productionplan['load'] = 'foo'
        serializer = ProductionPlanSerializerIn(data=self.productionplan)
        self.assertFalse(serializer.is_valid())

    def test_invalid_fuels(self):
        self.productionplan['fuels'] = 'foo'
        serializer = ProductionPlanSerializerIn(data=self.productionplan)
        self.assertFalse(serializer.is_valid())

    def test_invalid_powerplants(self):
        self.productionplan['powerplants'] = 'foo'
        serializer = ProductionPlanSerializerIn(data=self.productionplan)
        self.assertFalse(serializer.is_valid())
    
    def test_missing_fuels(self):
        del self.productionplan['fuels']
        serializer = ProductionPlanSerializerIn(data=self.productionplan)
        self.assertFalse(serializer.is_valid())

    def test_missing_powerplants(self):
        del self.productionplan['powerplants']
        serializer = ProductionPlanSerializerIn(data=self.productionplan)
        self.assertFalse(serializer.is_valid())
