from django.urls import path
from catalog import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

app_name = 'catalog'
urlpatterns = [
    path('', views.HomePageView.as_view(), name="home"),
    path('catalog/', views.CatalogView.as_view(), name="catalog"),
    path('catalog/<int:pk>/', views.DetailView.as_view(), name="detail"),
    path('genre/<int:pk>/', views.GenreView.as_view(), name="genre"),
    path('about/', views.about, name="about"),
    path('recommendations/', views.recommendations, name="recommendations"),
]

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns() + static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
)