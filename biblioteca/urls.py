from django.contrib import admin
from django.urls import include, path
from app import views
# from django.conf import settings
# from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('eventos/', include('eventos.urls')),
    
]

# if not settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
