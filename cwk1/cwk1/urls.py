from django.contrib import admin
from django.urls import path, include  # 确保 include 被导入

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('ratings.urls')),  # 这里使用 include
]
