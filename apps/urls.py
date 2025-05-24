from django.contrib import admin
from django.urls import path,re_path
from .views import baloncapitalino_view, femenino_view, unica_view, kids_view
from django.conf import settings
from django.conf.urls.static import static
from .views import JugadorListAPIView
from .views import busqueda_jugadores
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="API Balón Capitalino",
      default_version='v1',
      description="Documentación de la API de jugadores",
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', baloncapitalino_view, name='baloncapitalino'),
    path('femenino/', femenino_view, name='femenino'),
    path('unica/', unica_view, name='unica'),
    path('kids/', kids_view, name='kids'),
    path('api/jugadores/', JugadorListAPIView.as_view(), name='jugador-list'),
    path('busqueda/', busqueda_jugadores, name='busqueda'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)