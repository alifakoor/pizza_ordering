from django.urls import path
from . import views

urlpatterns = [
    path("", views.OrdersListView.as_view(), name="orders.list"),
	path("<int:pk>", views.OrdersDetailView.as_view(), name="orders.detail"),
    path("new", views.OrdersCreateView.as_view(), name="orders.new"),
    path("<int:pk>/edit", views.OrdersUpdateView.as_view(), name="orders.update"),
    path("<int:pk>/delete", views.OrdersDeleteView.as_view(), name="orders.delete"),
	path("<int:pk>/cancel", views.OrdersDeleteView.as_view(), name="orders.cancel"),
]