from django.urls import path

from . import views


urlpatterns = [
    # ex: api/
    path("students/", views._student_all),
    path("staff/", views._staff_all),
    path("clear_stud/", views._clear_stud),
    path("clear_staf/", views._clear_staf),
]
