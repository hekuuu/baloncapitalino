from django.contrib import admin
from django.urls import path
from .views import baloncapitalino_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', baloncapitalino_view, name='baloncapitalino'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)