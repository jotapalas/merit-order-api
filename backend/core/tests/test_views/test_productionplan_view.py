from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse


class ProductionPlanViewTestCase(APITestCase):
    def setUp(self):
        super().setUp()
        self.payload = {
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

        self.url = reverse('productionplan')


    def test_productionplan(self):
        expected_response = [
            {
                "name": "windpark1",
                "p": 90.0
            },
            {
                "name": "windpark2",
                "p": 21.6
            },
            {
                "name": "gasfiredbig1",
                "p": 460.0
            },
            {
                "name": "gasfiredbig2",
                "p": 338.4
            },
            {
                "name": "gasfiredsomewhatsmaller",
                "p": 0.0
            },
            {
                "name": "tj1",
                "p": 0.0
            }
        ]
        response = self.client.post(self.url, self.payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, expected_response)

    def test_invalid_payload(self):
        response = self.client.post(self.url, {}, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
