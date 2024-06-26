from rest_framework import serializers
from .models import UploadedImage, productoDb

class ProductoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = productoDb
        fields = "__all__"
        
class UploadedImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadedImage
        fields = ['id', 'image', 'uploaded_at']



        
    