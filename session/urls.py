from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.shortcuts import redirect
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('maths/',  include('maths.urls')),
    path('physics/', include('physics.urls')),
    path('', lambda request: redirect('maths/', permanent=False)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
