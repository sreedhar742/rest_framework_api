from rest_framework import serializers
from .models import Store,Hello

class Storeser(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Store
        fields='__all__'
        
        
class Petuser(serializers.ModelSerializer):
    class Meta:
        model=Hello
        fields="__all__"


