from django.contrib import admin
from django.urls import include, path

from rest_framework.documentation import include_docs_urls
from rest_framework.schemas import get_schema_view
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_swagger.views import get_swagger_view

API_TITLE = 'Blog API'  # new
API_DESCRIPTION = 'A Web API for creating and editing blog posts.'  # new
schema_view = get_swagger_view(title=API_TITLE)


urlpatterns = [
    # Admins
    path('admin/', admin.site.urls),

    # Route doesn't matter here, but allows login/logout of browsable API
    path('api-auth/', include('rest_framework.urls')),

    # Auth
    path('api/v1/api-token-auth/', obtain_jwt_token),
    path('api/v1/rest-auth/', include('rest_auth.urls')),
    path('api/v1/rest-auth/registration/',
         include('rest_auth.registration.urls')),

    # posts
    path('api/v1/', include('posts.urls')),

    # Docs
    path('api/v1/docs/', include_docs_urls(title='Blog API')),  # new
    path('api/v1/swagger-docs/', schema_view),  # new
]
