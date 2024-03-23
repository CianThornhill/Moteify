from django.urls import path
from .views import profile_view, delete_account

app_name = 'profiles'

urlpatterns = [
    path('', profile_view, name='profile_view'),
    path('delete_account/', delete_account, name='delete_account'),
]
