from django.urls import path, include

app_name = "api-v1"

urlpatterns = [
    path("user", include("accounts.api.v1.urls.accounts")),
    # path("profile/", include("accounts.api.v1.urls.profile")),
]
