from django.urls import path

from . import views

urlpatterns = [
    path('v1/rights/', views.RightList.as_view()),
    path('v1/right/', views.RightView.as_view()),
]
