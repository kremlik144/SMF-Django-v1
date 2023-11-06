from django.urls import path
from .views import index, user_form, many_fields_form, add_user, upload_image


urlpatterns = [
    path('', index, name='index'),
    path('user/add/', user_form, name='user_form'),
    path('forms/', many_fields_form, name='many_fields_form'),
    path('user/', add_user, name='add_user'),
    path('upload/', upload_image, name='upload_image'),


    # path('posts/<int:post_id>', post_full, name='post_full'),
]