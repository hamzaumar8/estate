from django.urls import path, include
from .views import  user, admin

app_name = 'dashboard'

# Admin
urlpatterns = [
    path("", user.dashboard, name="dashboard"),

    # Homes
    path("home/", admin.Homes, name="homes"),
    path("home/add/", admin.AddHome, name="add-home"),
    path("home/<int:id>/edit/", admin.EditHome, name="edit-home"),
    path("home/<int:id>/view/", admin.ViewHome, name="view-home"),
    path("home/<int:id>/delete/", admin.DeleteHome, name="delete-home"),
]