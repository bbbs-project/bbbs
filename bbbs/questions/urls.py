from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

v1_router = DefaultRouter()
v1_router.register('questions', views.QuestionListViewSet, basename='questions')
v1_router.register('questions/tags', views.TagViewSet, basename='tags')
v1_router.register('question', views.QuestionCreateViewSet, basename='question')

urlpatterns = [
    path('v1/', include(v1_router.urls)),
]
