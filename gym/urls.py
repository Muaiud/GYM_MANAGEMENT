from django.urls import path
from . import views


urlpatterns = [
    path('', views.LogIn, name='login'),
    path('signup/', views.SignUp, name="signup"),
    path("homepage/", views.Homepage, name="Homepage")
]
