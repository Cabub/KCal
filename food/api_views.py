from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication, \
                                          BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializers import FoodSerializer, PortionSerializer, \
                         NutritionFactSerializer

from .models import Food, Portion, NutritionFact


class FoodViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows foods to be viewed or edited.
    """
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated, )
    queryset = Food.objects.all()
    serializer_class = FoodSerializer


class PortionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows portions to be edited or viewed.
    """
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated, )
    queryset = Portion.objects.all()
    serializer_class = PortionSerializer


class NutritionFactViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows NutritionFacts to be edited or viewed.
    """
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated, )
    queryset = NutritionFact.objects.all()
    serializer_class = NutritionFactSerializer
