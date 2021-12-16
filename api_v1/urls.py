from django.contrib import admin
from django.urls import path, re_path, include
from .views import *

urlpatterns = [
    re_path(r'test-endpoint/?', Test.as_view(), name="test"),
]
