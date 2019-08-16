from django.conf.urls import url, include
from django.urls import path, include
from django.contrib import admin
from django.views.generic import RedirectView
from django.views.static import serve
from django.views.generic.base import TemplateView
from .settings import MEDIA_ROOT


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('antiqueProjectApp.urls')),
    path('accounts/', include('accounts.urls')),
    # For authentication management
    path('accounts/', include('django.contrib.auth.urls')),
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
    url(r'^$', RedirectView.as_view(url='antiqueProjectApp/')),
    url(r'antiqueProjectApp/', include('antiqueProjectApp.urls')),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT})
]