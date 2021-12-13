from django.urls import path
from apps.search import views

urlpatterns = [
    path('search/', views.CreateSearch.as_view()),      #post method, create search
    path('first/search/', views.FirstSearch.as_view()), # get first search 
    path('last/search/', views.LastSearch.as_view()),   # get last search
    path('most/search/', views.MostSearch.as_view()),   # get 5 most searchs
    path('total/search/', views.TotalSearch.as_view()),   # get total searchs
]
