from django.urls import path
from .views import delete

app_name = "comments"

urlpatterns = [
    path("<int:id>", delete, name="delete"),
]
