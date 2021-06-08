from django.urls import path

from .views import (
    OrganizationListCreateView,
    OrganizationRetrieveUpdateDelete,
)

app_name = "organizations"
urlpatterns = [
    path("", view=OrganizationListCreateView.as_view()),
    path("<int:pk>/", view=OrganizationRetrieveUpdateDelete.as_view()),
]
