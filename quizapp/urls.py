from django.urls import path
from . import views

# Comment goes here

urlpatterns = [
    path('', views.landing, name='landing'),  # Homepage
    path('signup/', views.sign_up, name='signup'),  # Signup page
    path('login/', views.log_in, name='login'),  # Login page
]