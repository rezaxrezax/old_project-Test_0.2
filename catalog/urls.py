from django.urls import path

#from .import views
from catalog import views


app_name = 'catalog'

urlpatterns = [
    #----------TEST----------#
    path('1/', views.basic_one, name='basic_one'),
    path('2/', views.basic_two, name='basic_two'),
    path('3/', views.basic_three, name='basic_three'),
    #-------------------------------------------------#
    path('articles/all/', views.articles, name='articles'),
    path('articles/get/<article_id>/', views.article, name='article'),
    path('articles/addcomment/<article_id>/', views.addcomment, name='addcomment'),
    path('page/<page_number>/', views.articles, name='article'),
    path('', views.articles, name='articles'),
]