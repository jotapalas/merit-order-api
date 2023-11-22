from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from rest_framework import status
from core.serializers import ProductionPlanSerializerIn
from core.utils import calculate_merit_order

class ProductionPlanView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        try:
            serializer = ProductionPlanSerializerIn(data=request.data)
            serializer.is_valid(raise_exception=True)
            input_data = serializer.validated_data
            data = calculate_merit_order(
                load=input_data['load'],
                fuels=input_data['fuels'],
                powerplants=input_data['powerplants']
            )

            response = Response(data, status=status.HTTP_200_OK)
        except ValidationError as e:
            response = Response(
                str(e), status=status.HTTP_400_BAD_REQUEST
            )

        return response
