# 프로젝트의 URL 라우팅 정의
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('stream.urls')),
]
