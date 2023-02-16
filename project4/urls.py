from django.contrib import admin
from django.urls import path

from auth_api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.LoginView.as_view()),
    path('logout/', views.LogoutView.as_view()),
    path('signup/', views.SignUpView.as_view()),
    path('profile/', views.ProfileView.as_view())
]
