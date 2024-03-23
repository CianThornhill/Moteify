from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("home.urls")),
    path("accounts/", include("allauth.urls")),
    path('profiles/', include('profiles.urls')),
    path('djrichtextfield/', include('djrichtextfield.urls')),
    path('emotes/', include('emotes.urls')),
]
