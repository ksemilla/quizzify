from django.urls import path

from .views import (
    OrganizationListCreateView
)

app_name = "organizations"
urlpatterns = [
    path("", view=OrganizationListCreateView.as_view()),
]
