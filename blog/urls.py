from django.urls import path
from . import views
from .feeds import LatestPostsFeed

app_name = 'blog'
urlpatterns = [
    path('', views.post_list, name='post_list'),
    path(
        'tag/<slug:tag_slug>/', views.post_list, name='post_list_by_tag'
    ),
    # path(
    #     '', 
    #     views.PostListView.as_view(), 
    #     name='post_list'
    # ),
    path(
        '<int:year>/<int:month>/<int:day>/<slug:post>/', 
        views.post_detail, 
        name='post_detail'
    ),
    path(
        '<int:post_id>/share/', 
        views.post_share, 
        name='post_share'
    ),
    path(
        '<int:post_id>/comment/',
        views.post_comment,
        name='post_comment'
    ),
    path('feed/', LatestPostsFeed(), name='post_feed'),
    path('search/', views.post_search, name='post_search'),
]

EMAIL_HOST_USER=emmiduh93@gmail.com
EMAIL_HOST_PASSWORD=cnvrvgvtqwggbkdr
DEFAULT_FROM_EMAIL=My Blog <myblog@gmail.com>
DB_NAME=blog
DB_USER=blog
DB_PASSWORD=blog
DB_HOST=localhost
SECRET_KEY=django-insecure-bq817^e5q$_51d-kw2^d&(fre94+e_-ovygpskq)#*a%3ww#v_
postgresql://blog:h7xZr3Ms5WDabJdo9ioijhrua6TEK3sf@dpg-d5svnh5actks73a66n3g-a.oregon-postgres.render.com/blog_dktk
