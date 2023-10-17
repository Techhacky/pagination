from django.urls import path,re_path,include
from .views import  PaginationView
urlpatterns = [

    path('page',PaginationView.as_view()),
    path('page/<int:pk>',PaginationView.as_view()),


]