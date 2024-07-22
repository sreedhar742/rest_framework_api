from django.shortcuts import render

from rest_framework import viewsets
from .models import Store,Hello
from .serializers import Storeser,Petuser


class Storeview(viewsets.ModelViewSet):
    queryset=Store.objects.all()
    serializer_class=Storeser
     
from rest_framework import viewsets
from .models import Hello
from .serializers import Petuser

class Petview(viewsets.ModelViewSet):
    queryset = Hello.objects.all()
    serializer_class = Petuser

from django.db import connection
def your_view(request):
    print(connection.queries)
    
    
import requests
def index(request):
    response=requests.get('http://127.0.0.1:8000/stores/')
    data=response.json()
    return render(request,"index.html",{'data':data})
