
from django.urls import path
from publication import views

urlpatterns = [
    path('book-api/',views.BooksAPI.as_view()),
    path('register/',views.RegisterUser.as_view()),
]