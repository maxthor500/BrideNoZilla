from . import views
from django.urls import path

urlpatterns = [
    path("", views.view_events, name="view_events"),
    path("post/<int:post_id>/", views.view_post, name="view_post"),
    path("post/<int:post_id>delete/comment/",
         views.delete_comment, name="delete_comment"),
    path("add/post/", views.add_post, name="add_post"),
    path("edit/post/<int:post_id>/", views.edit_post, name="edit_post"),
    path("delete/post/<int:post_id>/", views.delete_post, name="delete_post"),
]
