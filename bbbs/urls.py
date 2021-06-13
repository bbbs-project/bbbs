import os
from django.contrib import admin
from django.urls import path, re_path
from django.urls.conf import include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from dotenv import load_dotenv

load_dotenv()

schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email=os.getenv('EMAIL')),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
)


urlpatterns = [
    path('admin/', admin.site.urls),

    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(
        cache_timeout=0
    ), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui(
        'swagger', cache_timeout=0
    ), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui(
        'redoc', cache_timeout=0
    ), name='schema-redoc'),
    path('api/', include('bbbs.afisha.urls')),
    path('api/', include('bbbs.common.urls')),
    path('api/', include('bbbs.main.urls')),
    path('api/', include('bbbs.rights.urls')),
]
