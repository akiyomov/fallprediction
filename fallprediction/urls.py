from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include('api.urls')),
    path('api-auth/',include('rest_framework.urls')),
    path('api/dj-rest-auth/',include('dj_rest_auth.urls')),
    path('api/dj-rest-auth/registeration/',include('dj_rest_auth.registration.urls')),
    path('api/allauth/',include('allauth.urls')),
] 

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

