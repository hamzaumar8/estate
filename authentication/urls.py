from django.urls import path, include
from .views import registration

app_name = 'authentication'

# Admin
urlpatterns = [
    # path("", user.dashboard, name="dashboard"),
    
    path("signup/<str:token>/", registration, name="signup"),
]