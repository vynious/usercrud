from . import views
from django.urls import path

urlpatterns = [
    path('', views.user_home, name='home'),
    # path('register/',views.RegisterAPI.as_view(), name='register'),
    path('register/',views.registration, name='register'),
    path('detail/', views.detail, name='detail'),
    path('update/', views.update, name='update'),
    path('delete/', views.delete, name='delete'),

]
