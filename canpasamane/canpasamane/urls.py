from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('usuari.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]+static('/static/', document_root=settings.STATIC_ROOT, show_indexes=True)