from django.urls import path
from . import views

urlpatterns = [
    path("", views.PizzaListView.as_view(), name="pizza.list"),
]