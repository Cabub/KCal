from . import api_views


def register_routes(router):
    router.register(r'auth/groups', api_views.GroupViewSet)
    router.register(r'auth/users', api_views.UserViewSet)
