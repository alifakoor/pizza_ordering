from datetime import datetime
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect

from .forms import OrdersForm
from .models import Order


class OrdersListView(LoginRequiredMixin, ListView):
    model = Order
    context_object_name = "orders"
    template_name = "orders_list.html"
    login_url = "/login"

    def get_queryset(self):
        orders = self.request.user.orders.all()
        received = orders.filter(status__exact='r')
        preparing = orders.filter(status__exact='p')
        delivered = orders.filter(status__exact='d')
        return {"received": received, "preparing": preparing, "delivered": delivered}


class OrdersDetailView(DetailView):
    model = Order
    template_name = "order_detail.html"
    context_object_name = "order"


class OrdersCreateView(CreateView):
    model = Order
    template_name = "order_form.html"
    success_url = '/orders'
    form_class = OrdersForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.customer = self.request.user
        self.object.status = "r"
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class OrdersUpdateView(UpdateView):
    model = Order
    success_url = '/orders'
    form_class = OrdersForm


class OrdersDeleteView(DeleteView):
    model = Order
    context_object_name = "order"
    success_url = '/orders'
    template_name = 'order_delete.html'
