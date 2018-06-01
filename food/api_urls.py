from . import api_views


def register_routes(router):
    router.register(r'food/food', api_views.FoodViewSet)
    router.register(r'food/portion', api_views.PortionViewSet)
    router.register(r'food/nutritionfact', api_views.NutritionFactViewSet)
