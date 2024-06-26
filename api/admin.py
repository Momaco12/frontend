from django.contrib import admin
from .models import productoDb

# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    fields = ["nombre","precio","descripcion","proveedor","imagen","codigo"]
    list_display = ["nombre","precio","descripcion","proveedor","imagen","codigo"]

admin.site.register(productoDb,)


