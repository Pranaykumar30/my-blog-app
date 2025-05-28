from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    path('post/new/', views.create_post, name='create_post'),
    path('post/<int:post_id>/edit/', views.edit_post, name='edit_post'),
    path('post/<int:post_id>/delete/', views.delete_post, name='delete_post'),
    path('test-login/', views.test_login_page, name='test_login'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('users/<str:username>/', views.public_profile, name='public_profile'),
    path('authors/', views.authors_list, name='authors_list'),
]