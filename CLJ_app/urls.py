from django.urls import path
from . import views

# CLJ_app urls.py

urlpatterns = [
    #categories URLs
    path('', views.categories, name='categories'),
    path('<int:category_id>/', views.category_details, name='category_detail'),
    path('new/', views.new_category, name='new_category'),
    path('<int:category_id>/edit/', views.category_edit, name='category_edit'),
    path('<int:category_id>/delete/', views.category_delete, name='category_delete'),


    # posts URL
    path('posts', views.posts, name='posts'),
    path('<int:category_id>/posts/<int:post_id>/', views.post_detail, name='post_detail'),
    path('<int:category_id>/posts/new/', views.new_post, name='new_post'),
    path('<int:category_id>/posts/<int:post_id>/edit/', views.post_edit, name='post_edit'), 
    path('<int:category_id>/posts/<int:post_id>/delete/', views.post_delete, name='post_delete')

]


    # /categories: A list of all the categories
    # /categories/new: The form for a new category
    # /categories/:id: See a specific category and a list of all of its associated posts
    # /categories/:id/edit: Edit page for a specific category
    # Also, the ability to update/destroy categories
    # /categories/:category_id/posts/new: The form for a new post under a specific category
    # /categories/:category_id/posts/:post_id: See a specific post for a specific category, have the ability go back to all of the post's category's other posts (/categories/:category_id/posts)
    # /categories/:category_id/posts/:post_id/edit: Edit page for a specific post under a specific category
    # Also, the ability to update/destroy posts