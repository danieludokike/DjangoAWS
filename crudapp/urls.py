from django.urls import path

from .views import home_view, add_task_view, update_task_view


app_name = "crud"
urlpatterns = [
    path("", home_view, name="home"),
    path("add-task/", add_task_view, name="add_task"),
    path("update-task/<int:task_id>/", update_task_view, name="update_task")
]
