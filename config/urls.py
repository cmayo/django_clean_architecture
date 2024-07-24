from django.contrib import admin
from django.urls import path
from ninja import NinjaAPI

api = NinjaAPI()

api.add_router("/demo", "src.demo.infrastructure.ui.api.demo_router")
api.add_router("/auth", "src.auth.infrastructure.ui.api.auth_router")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", api.urls),
]
