from django.urls import path
from core.views import (
    ProductionPlanView
)


urlpatterns = [
    path(
        'productionplan', ProductionPlanView.as_view(),
        name='productionplan'
    ),
]
