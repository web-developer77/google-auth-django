from django.urls import path
from googleauthapp import views

app_name = "googleauthapp"

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
]