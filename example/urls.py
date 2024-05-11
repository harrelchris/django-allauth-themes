from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView

urlpatterns = [
    path("", TemplateView.as_view(template_name="views/index.html"), name="index"),
    path(
        "accounts/profile/",
        TemplateView.as_view(template_name="views/profile.html"),
        name="profile",
    ),
    path("accounts/", include("allauth.urls")),
    path("admin/", admin.site.urls),
]
