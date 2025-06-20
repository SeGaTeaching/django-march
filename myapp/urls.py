from django.urls import path
from . import views

urlpatterns = [
    path("", views.app, name="home"),
    path("get/", views.get_query, name="get_query"),
    path("form/example/", views.form_example, name="form_example"),
    path("marion/", views.marion, name="marion"),
    path("john/", views.john, name="john"),
    path("<str:name>/", views.user, name="user"),
    path("product/<int:product_id>/", views.product_details),
]
