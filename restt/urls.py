from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import Storeview, Petview,index,index2

router = DefaultRouter()
router.register(r'stores', Storeview, basename='store')
router.register(r'pettaker', Petview, basename='pettaker')

urlpatterns = [
    path('', include(router.urls)),
    path('index/',index,name="index"),
    path('pets/',index2,name='pets')
]
