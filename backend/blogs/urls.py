from django.urls import path
from . import views

urlpatterns = [
    path("list/", views.BlogsList.as_view(), name="blogs"),
    path("author/", views.AuthorList.as_view(), name="authors")
]