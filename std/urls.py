from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("home/", views.home, name="home"),
    path("add-std/", views.std_add, name="add_std"),
    path("delete-std/<int:id>/", views.delete_std, name="delete_std"),
    path("update-std/<int:id>/", views.update_std, name="update_std"),
    path("do-update-std/<int:id>/", views.do_update_std, name="do_update_std"),
]