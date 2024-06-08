from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_page, name="home"),
    path("songs/<slug:category>", views.songs_cat_page, name="songs_cat"),
    path("songs/playlist/<slug:playlist>", views.songs_page, name="songs_playlist"),
    path("song/<slug:title>", views.song_page, name="song"),
    path("artists", views.artists_page, name="artists"),
    path("artist/<slug:name>", views.artist_page, name="artist")
]