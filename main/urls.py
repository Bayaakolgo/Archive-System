from django.urls import path
from . import views

urlpatterns = [
    path('',views.login_request, name='login'),
    path('register/', views.register_request, name='register'),
    path('logout/', views.logout_request, name='logout'),
    path('dashboard/', views.dashboard_request, name='dashboard'),
    path('upload/', views.upload_request, name='upload'),
    path('download/<int:pk>/', views.download_request, name='download'),
    path('delete/<int:pk>/', views.delete_request, name='delete'),

]

