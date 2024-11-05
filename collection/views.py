from rest_framework import viewsets
from .models import Shirt, Pant, Shoe
from .serializers import ShirtSerializer, PantSerializer, ShoeSerializer

class ShirtViewSet(viewsets.ModelViewSet):
    queryset = Shirt.objects.all()
    serializer_class = ShirtSerializer

class PantViewSet(viewsets.ModelViewSet):
    queryset = Pant.objects.all()
    serializer_class = PantSerializer

class ShoeViewSet(viewsets.ModelViewSet):
    queryset = Shoe.objects.all()
    serializer_class = ShoeSerializer
    
