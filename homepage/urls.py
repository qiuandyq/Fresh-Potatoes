from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name="home"),
    path('about/', views.about, name="about"),
    path('FAQ/', views.faq, name="faq") # add in FAQ page path 
]