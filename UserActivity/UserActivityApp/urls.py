from rest_framework.routers import DefaultRouter

from . import views
""" connecting to DefaultRouter where  each-viewsets is registered with the router with given prefix """
router = DefaultRouter()
router.register(r'userActivity', views.UserViewSet)
