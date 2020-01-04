from django.urls import path, include

from . import views, serializers


urlpatterns = [
    # ex: api/
    path("", views.index),
    path("verify_student/", views._verify_stud),
    path("verify_staff/", views._verify_staff),
    path("d_stud/", views.show_full_details_student),
    path("d_staf/", views.show_full_details_staff),
]
