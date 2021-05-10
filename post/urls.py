from django.urls import path
from . import views
app_name='post'
urlpatterns = [
    path('all/',views.all_posts,name='posts'),
]
