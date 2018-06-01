from rest_framework import serializers
from .models import Food, Portion, NutritionFact


class FoodSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Food
        fields = ('name', )


class PortionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Portion
        fields = ('portion', )


class NutritionFactSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = NutritionFact
        fields = ('name', 'food', 'portion', 'count', )
