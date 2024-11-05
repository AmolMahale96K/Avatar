from rest_framework import serializers
from .models import Shirt, Pant, Shoe

class ShirtSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shirt
        fields = ['id', 'shirt_name', 'shirt_type', 'image', 'created_at']

class PantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pant
        fields = ['id', 'pant_name', 'pant_type', 'image', 'created_at']

class ShoeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shoe
        fields = ['id', 'shoe_name', 'shoe_type', 'image', 'created_at']


