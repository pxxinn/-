from django.urls import path
from .views import *

urlpatterns = [
    path("",ArticleView.as_view(), name="index"),
    path('category/<int:pk>/',ArticleByCategory.as_view(), name="category"),
    path('article/<int:pk>/',ArticleDetail.as_view(), name="article"),
    path('profile/',profile, name="profile"),
    path('logout/',user_logout, name="logout"),
    path('login/',user_login, name="login"),
    path('register/',user_register, name="register"),
    path('add_article/',AddArticle.as_view(), name="add_article"),
    path('delete/<int:pk>/',DeleteArticle.as_view(), name="delete"),
    path('edit/<int:pk>/',EditArticle.as_view(), name="edit"),
    path('add_comment/<int:article_id>/',save_comment, name="save_comment"),
    path('search/',SearchResult.as_view(), name="search_result"),
]
