from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProfessorViewSet, ModuleViewSet, ModuleInstanceViewSet, RatingViewSet
from .auth_views import CustomAuthToken 

# 使用 DefaultRouter 自动生成 API 端点
router = DefaultRouter()
router.register(r'professors', ProfessorViewSet)
router.register(r'modules', ModuleViewSet)
router.register(r'module_instances', ModuleInstanceViewSet)
router.register(r'ratings', RatingViewSet)

urlpatterns = [
    path('', include(router.urls)),  # 关键
    path('login/', CustomAuthToken.as_view(), name='login'),
]
