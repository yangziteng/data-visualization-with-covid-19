# from django.conf.urls import url
# from django.conf.urls import url

from django.urls import include, path

from rest_framework import routers
from . import views

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

app_name = 'covid'

urlpatterns = [
    path('statistics/', views.StatisticsListView.as_view(), name='statistics-list'),
    path('statistics/latest/',views.StatisticsView.as_view()),
    path('statistics/china/',views.StatisticsChinaView.as_view()),

    path('provinces/', views.ProvinceView.as_view(), name='province-list'),
    path('countries/', views.CountryRankView.as_view(), name='country-list'),
    path('worldtrend/', views.WorldTrendView.as_view()),
    path('chinatrend/', views.ChinaTrendView.as_view()),
   
]