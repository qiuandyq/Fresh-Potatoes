from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name="home"),
    path('about/', views.about, name="about"),
    path('FAQ/', views.faq, name="faq"), # add in FAQ page path
    path('more_info/<str:media_type>/<int:movie_id>/', views.more_info, ), # the <> brackets means the movie_num can be dynamic like a variable. Our int: means our input must be a string
    path('added_done/<str:media_type>/<int:movie_id>/', views.movie_added, name="added_movie_done"),
]