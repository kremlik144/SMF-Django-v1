from django.urls import path
from .views import hello, HelloViev, year_post, hello_name, son, son2, author_posts, post_full


urlpatterns = [
    path('hello1/', hello, name='hello1'),
    path('hello2/', HelloViev.as_view(), name='hello2'),
    path('hello3/', hello_name, name='hello3'),
    path('son1/', son, name='son'),
    path('son2/', son2, name='son2'),
    path('postss/<int:year>', year_post, name='year_post'),
    path('author/<int:author_id>', author_posts, name='author_posts'),
    path('posts/<int:post_id>', post_full, name='post_full'),
]
