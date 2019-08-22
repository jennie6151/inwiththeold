from django.urls import path
from . import views
from django.conf.urls import url, include
from .views import PurchaseAnItem


urlpatterns = [
  path('', views.index, name='index'),
  path('antiques/', views.AntiqueListView.as_view(), name='antiques'),
  path('Antique/<int:pk>', views.AntiqueDetailView.as_view(), name='antique-detail'),
  path('creators/', views.CreatorListView.as_view(), name='creators'),
  path('Creator/<int:pk>', views.CreatorDetailView.as_view(), name='creator-detail'),
  url(r'^(?P<pk>\d+)/new/$', PurchaseAnItem, name='NewSale'),
  path('charge/', views.charge, name='charge'),
]