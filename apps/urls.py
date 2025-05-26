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
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import scrape_jugadores
schema_view = get_schema_view(
    openapi.Info(
        title="Your API Title",
        default_version='v1',
        description="API documentation",
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
    path('', views.home, name='home'),
    
    path('busqueda/', busqueda_jugadores, name='busqueda'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += [
        path('scrape_jugadores/', scrape_jugadores, name='scrape_jugadores'),
    ]