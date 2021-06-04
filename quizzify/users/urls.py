from django.urls import path

from quizzify.users.views import (
    UserCreateView,
)

app_name = "users"
urlpatterns = [
    path("signup/", view=UserCreateView.as_view()),
]
