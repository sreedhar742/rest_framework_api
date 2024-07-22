from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import Storeview, Petview, index

router = DefaultRouter()
router.register(r'stores', Storeview, basename='store')
router.register(r'pettaker', Petview, basename='pettaker')

urlpatterns = [
    path('', include(router.urls)),
    path('index/',index,name="index")
]
