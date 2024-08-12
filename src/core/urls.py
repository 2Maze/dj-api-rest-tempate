from os import environ
from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions


api_url = environ.get('API_URL')
api_port = environ.get('API_PORT')


schema_view = get_schema_view(
    openapi.Info(
        title="API",
        default_version='v1',
        description="REST API.",
    ),
    url=f"http://{api_url}:{api_port}",
    public=True,  # False
    permission_classes=(permissions.AllowAny,),
    # permission_classes=(permissions.IsAdminUser,),
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('api.v1.urls')),
]


urlpatterns += [
    path('swagger/', schema_view().with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view().with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]