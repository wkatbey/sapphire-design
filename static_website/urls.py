from django.urls import path
from static_website.views import Home

app_name = 'static_website'
urlpatterns = [
    path('', Home.as_view(), name='index'),
]