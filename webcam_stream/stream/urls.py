# 'stream' 앱의 URL 라우팅 정의
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('live_stream', views.live_stream, name='live_stream'),
    path('get_object_location/', views.get_object_location, name='get_object_location'), 
    path('get_object_location2/', views.get_object_location2, name='get_object_location2'), 
]