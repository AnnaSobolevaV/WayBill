from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("home/", include("way_bills_creator.urls", namespace="way_bills_creator")),
    path("", include("users.urls", namespace="users")),
]
