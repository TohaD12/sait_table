from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('admin/', views.about, name='about'),
    path('create', views.create, name='create'),
    path('search', views.search, name='search'),
    path('create_accessories', views.create_accessories, name='create_accessories'),
    path('home_accessories', views.home_accessories, name='home_accessories'),
    path('search_accessories', views.search_accessories, name='search_accessories'),

]
