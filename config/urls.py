
from django.contrib import admin
from django.urls import include, path 
from blogapp.views import iletisim
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blogapp.urls')),
    path('account/', include('account.urls')),
    path('api/', include("blogapp.api.urls"))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
