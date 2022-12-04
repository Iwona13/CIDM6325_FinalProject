# from django.urls import path
# from .views import ImageDetailView

# urlpatterns = [
#     path("pictures/", ImageDetailView.as_view(), name="pictures"),
# ]

from django.urls import path
from . import views

urlpatterns = [
    path("pictures/", views.index, name="pictures"),
]
