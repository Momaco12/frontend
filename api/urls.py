from django.urls  import path,include
from rest_framework import routers
from api import views

router=routers.DefaultRouter()
router.register(r'productoDb',views.ProductoViewset)


urlpatterns = [
    path('',include(router.urls)),
    path('upload/', views.FileUploadView.as_view(), name='file-upload')
]