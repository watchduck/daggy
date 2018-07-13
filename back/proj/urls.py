from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from rest_framework import routers

from app import views

router = routers.DefaultRouter()
router.register(r'node', views.NodeViewSet, base_name='node')

urlpatterns = [

    url(r'^api/', include(router.urls)),

    url(r'^node-delete/(?P<node_id>[0-9]+)/$', views.delete_node_view),

    url(r'^node-allowed-relatives/$', views.node_allowed_relatives_view),

    url(r'^node-details/(?P<node_id>[0-9]+)/$', views.node_details_view),

    url(r'^admin/', admin.site.urls),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
