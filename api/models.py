from django.db import models

# Create your models here.

class productoDb(models.Model):
    nombre = models.CharField(max_length=75,verbose_name="Nombre")
    precio = models.DecimalField(verbose_name="Precio", max_digits=5, decimal_places=2, default=0)
    descripcion = models.TextField(verbose_name="Descripcion", max_length=75)
    proveedor = models.CharField(max_length=40, verbose_name="Proveedor", null=True, blank=True)
    imagen = models.TextField(verbose_name="Imagen", max_length=120, null=True, blank=True)
    fecha_entrega = models.DateField(verbose_name="Fecha_entrega")
    vendido = models.BooleanField(verbose_name="Vendido", default=False)
    fecha_venta = models.DateField(verbose_name="Fecha_venta", null=True, blank=True)
    codigo = models.IntegerField(verbose_name="Codigo", default=0)
    
    def __str__(self) -> str:
        return self.nombre

class UploadedImage(models.Model):
    image = models.ImageField(upload_to='images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
    
class Purchase(models.Model):
    PurchaseId = models.IntegerField(verbose_name="")

