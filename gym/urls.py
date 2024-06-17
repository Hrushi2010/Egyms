from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('program/<int:program_id>/', views.program_detail, name='program_detail'),
    



    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    # Add other paths here


]



