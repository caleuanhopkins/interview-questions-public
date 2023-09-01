from django.urls import path

from .views import AssignmentList

urlpatterns = [
    path("", AssignmentList.as_view()),
]