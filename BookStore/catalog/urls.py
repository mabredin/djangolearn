from django.urls import path
from catalog import views

app_name = 'catalog'
urlpatterns = [
    path('', views.HomePageView.as_view(), name="home"),
    path('genres/', views.GenresView.as_view(), name="genres"),
    path('about/', views.about, name="about"),
    path('recommendations/', views.recommendations, name="recommendations"),
]