from django.urls import path
from apps.search import views

urlpatterns = [
    path('search/', views.CreateSearch.as_view()),
    path('first/search/', views.FirstSearch.as_view()),
    path('last/search/', views.LastSearch.as_view()),
]
