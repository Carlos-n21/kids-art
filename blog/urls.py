from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('post/<slug:slug>/', views.post_detail, name='post_detail'),
    path('create/', views.create_post, name='create_post'),
    path('edit/<slug:slug>/', views.edit_post, name='edit_post'),
    path('delete/<slug:slug>/', views.delete_post, name='delete_post'),
    path('profile/', views.profile, name='profile'),
    path('approve_comment/<int:comment_id>/', views.approve_comment, name='approve_comment'),
    path('delete_comment/<int:comment_id>/', views.delete_comment, name='delete_comment'),
]