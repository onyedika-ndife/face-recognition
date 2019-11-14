from django.urls import path

from . import views

# APP NAME
app_name = "recognize"

urlpatterns = [
    # ex: /recognize/
    path("", views._upload, name="index")
]
