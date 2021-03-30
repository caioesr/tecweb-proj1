from django.urls import path

from . import views
from .models import Tag

all_tags = Tag.objects.all()

urlpatterns = [
    path('', views.index, name='index'),
]