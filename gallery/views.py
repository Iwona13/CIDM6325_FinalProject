from django.shortcuts import render
from .models import Image
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View


# class ImageDetailView(LoginRequiredMixin, View):
#     def index(request):
#         data = Image.objects.all()
#         context = {"data": data}
#         return render(request, "pictures.html", context)

#     def get(self, request):
#         return render(request, "pictures.html")


def index(request):
    data = Image.objects.all()
    context = {"data": data}
    return render(request, "pictures.html", context)
