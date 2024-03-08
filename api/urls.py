from django.contrib import admin
from django.urls import path

from api import views as api_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("contact/", api_views.ContactAPIView.as_view()),
    path("unique/balhamboxframes/", api_views.UserAuthView.as_view()),
    path(
        "unique/balhamboxframes/<str:jwt_token>/",
        api_views.UserAuthVerifyView.as_view(),
    ),
]
