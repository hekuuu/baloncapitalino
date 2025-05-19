from django.contrib import admin
from django.urls import path
from .views import baloncapitalino_view, femenino_view, unica_view, kids_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', baloncapitalino_view, name='baloncapitalino'),
    path('femenino/', femenino_view, name='femenino'),
    path('unica/', unica_view, name='unica'),
    path('kids/', kids_view, name='kids'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)