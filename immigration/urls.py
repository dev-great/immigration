from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from django.conf.urls.static import static

schema_view = get_schema_view(
    openapi.Info(
        title="Temu Immigration API Documentation",
        default_version='v1',
        description="...",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="developer@temuimmigration.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/authorization/', include('authentication.urls')),

]


urlpatterns += [
    path('api/v1/docs/', schema_view.with_ui('swagger',
         cache_timeout=0), name='schema-swagger-ui'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = 'Temu Immigration Control Panel'
admin.site.index_title = 'Administrators Dashboard'
admin.site.site_title = 'Control Panel'
