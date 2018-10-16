from django.urls import path

from . import views

urlpatterns = [
    path('', views.ListItem.as_view()),
    path('<int:pk>/', views.DetailItem.as_view()),
    path('/add-item', views.DetailItem.as_view()),
]