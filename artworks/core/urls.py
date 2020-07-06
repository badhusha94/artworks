from django.urls import path, include
from core.views import CustomerList,CutomerViewSet
from rest_framework import routers

artwork_router = routers.DefaultRouter()
artwork_router.register('customers',CutomerViewSet)

urlpatterns = [
    path('',include(artwork_router.urls))
]