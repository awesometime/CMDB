from django.urls import path
from assets import views

app_name = 'assets'

urlpatterns = [
    path(r'', views.dashboard),
    path(r'report/', views.report, name='report'),
    path(r'dashboard/', views.dashboard, name='dashboard'),
    path(r'index/', views.index, name='index'),
    path(r'detail/<int:asset_id>/', views.detail, name="detail"),

]