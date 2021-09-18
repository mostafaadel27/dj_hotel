from django.urls import path
from .views import Posts ,Post_detail , PostByCategory, PostByTags
app_name='blog'
urlpatterns = [
    path('',Posts.as_view(),name='post_list'),
    path('<slug:slug>',Post_detail.as_view(),name='post_detail'),
    path('category/<str:slug>',PostByCategory.as_view(),name='post_by_category'),
    path('tag/<slug:slug>',PostByTags.as_view(),name='post_by_tag')
]
