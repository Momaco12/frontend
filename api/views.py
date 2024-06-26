from django.shortcuts import render
from .serializer import ProductoSerializer
from rest_framework import viewsets
from .models import productoDb

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status
from .models import UploadedImage
from .serializer import UploadedImageSerializer
import cv2
from pyzbar.pyzbar import decode

# Create your views here.

def analize(images):
        image = cv2.imread(images)

            # # Convert to grayscale (optional, but might improve detection)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

            # # Detect barcodes
        barcodes = decode(gray)

            # # Process and display results
        if barcodes:
            for barcode in barcodes:
                (x, y, w, h) = barcode.rect
                cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
                data = barcode.data.decode("utf-8")
                cv2.putText(image, data, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
                print(f"Decoded Data: {data}")
                result = data
                return result
        else:
            print("No barcodes found in the image.")
class ProductoViewset(viewsets.ModelViewSet):
    queryset = productoDb.objects.all()
    
    serializer_class=ProductoSerializer
    
#class PlantillaViewset(viewsets.ModelViewSet):
   # queryset = plantillaDb.objects.all()
    
    #serializer_class=PlantillaSerializer


class FileUploadView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    
    
    
    def post(self, request, *args, **kwargs):
        file_serializer = UploadedImageSerializer(data=request.data)
        if file_serializer.is_valid():
            file_serializer.save()
            
            
            print(file_serializer)
            
            datas = file_serializer.data
            # id = datas['id']
            url = datas['image']
            # time = datas['uploaded_at']
            
            result = analize('./img/codigo1.png')
            
            if result :
                producto  = productoDb.objects.get(codigo=result)
                producto_serializer = ProductoSerializer(producto)
            
        
            
            
            return Response(producto_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
