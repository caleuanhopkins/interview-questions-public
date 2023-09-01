from django.urls import path

from .views import ListingList

urlpatterns = [
    path("", ListingList.as_view()),
    path("<int:id>", ListingList.as_view())
]