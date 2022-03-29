from django.urls import path
from catalog import views


urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
]