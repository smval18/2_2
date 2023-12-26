from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.IndexList.as_view(), name="index"),
    path('', include('django.contrib.auth.urls')),
    path('service/', views.ServiceList.as_view(), name="services"),
    path('service/<int:id>/', views.service_detail, name='services-detail'),
    path('register/', views.RegisterView.as_view(), name="register"),
    path('profile/', views.profile, name="profile"),

]
