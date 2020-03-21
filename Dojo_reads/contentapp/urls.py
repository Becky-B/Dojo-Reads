from django.urls import path
from .import views

urlpatterns = [
    path('', views.index),
    path('/add', views.add_page),
    path('/add_book_review', views.add_book),
    path('/<int:book_id>', views.book_info),
    path('/review/<int:book_id>', views.review),
    path('/delete/<int:review_id>/<int:book_id>', views.delete_review),
    path('/user/<int:users_id>', views.user_info_page)
]