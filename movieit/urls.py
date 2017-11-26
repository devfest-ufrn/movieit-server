from django.conf.urls import url, include
from .movies.urls import movie_routers
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='MovieIt API')

urlpatterns = [
    url(r'^$', schema_view),
    url(r'^', include(movie_routers.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]




