from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("entregas/", include("entregas.urls")),
    path("", include("entregas.urls")),
]
