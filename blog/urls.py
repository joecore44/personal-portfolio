from django.urls import path
from .views import SinglePostView
from . import views


urlpatterns = [
    path('', views.home, name='blog-home'),
    path('post/<int:pk>/', SinglePostView.as_view(), name='post-detail'),
]

