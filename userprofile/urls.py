from django.urls import path
from .views import logout_view, register, login_view, profile

app_name="userprofile"
urlpatterns = [
    path('register/', register, name="register"),
    path('login/', login_view, name="login"),
    path('profile/', profile, name="profile"),
    path('logout/', logout_view, name="logout"),    
]
