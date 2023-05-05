from typing import Any, Dict
from django import forms
from django.forms.models import BaseModelForm
from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views.generic import ListView, CreateView, DetailView
from orders.models import Vehicle, Order, Details
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user
from django.contrib.auth.decorators import login_required
from django.db.models import Q
import logging
import matplotlib.pyplot as plt
import seaborn as sns


# Create your views here.
def get_current_user_id(request):
    user = get_user(request)
    if user.is_authenticated:
        return user.id
    return None


class ProductListView(ListView):
    model = Details
    template_name = 'product_list.html'
    context_object_name = 'details'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        q = self.request.GET.get('q')
        if q:
            queryset = queryset.filter(
                Q(vehicle__name__icontains=q) | Q(year__icontains=q)
            )
        return queryset

class OrderCreateView(LoginRequiredMixin ,CreateView):

    quantity = forms.IntegerField(initial=1)
    model = Order
    fields = ['address', 'quantity']
    template_name = 'order_form.html'

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
      
        detail_id = self.request.POST.get('detail_id')
        user_name = self.request.POST.get('user_name')
        user_email = self.request.POST.get('user_email')
        

     
        try:
            detail = Details.objects.get(pk=detail_id)
            form.instance.name = user_name
            form.instance.email = user_email
            form.instance.product = detail
            form.instance.user = self.request.user
            logging.debug(f'detail={detail}')
        except Details.DoesNotExist:
            logging.error(f'Details matching query does not exist for detail_id={detail_id}')
            raise Http404('Details not found')
        return super().form_valid(form)
    
    def get_success_url(self) -> str:
        return reverse('order_detail', args=[self.object.pk])
    
class OrderDetailView(DetailView):
    model = Order
    template_name = 'order_detail.html'
    context_object_name = 'order'


class OrderHistoryView(LoginRequiredMixin, ListView):
    model = Order
    template_name = 'order_history.html'
    context_object_name = 'orders'

    def get_queryset(self):
        start_date = self.request.GET.get('start_date')
        end_date = self.request.GET.get('end_date')
        queryset = Order.objects.filter(user=self.request.user)

        if start_date:
            queryset = queryset.filter(date_ordered__gte=start_date)

        if end_date:
            queryset = queryset.filter(date_ordered__lte=end_date)

        return queryset.order_by('-date_ordered')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['start_date'] = self.request.GET.get('start_date')
        context['end_date'] = self.request.GET.get('end_date')
        return context
        

class VehicleDetailView(DetailView):
    model = Vehicle
    template_name = 'vehicle_detail.html'
    context_object_name = 'vehicle'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        vehicle = self.get_object()
        detail_id = self.kwargs.get('detail_id')
        context['details'] = Details.objects.filter(vehicle=vehicle, id=detail_id)
        return context
    
#function to compare vehicles
def compare(request):
    if request.method == 'POST':
        vehicle1_id = request.POST.get('vehicle1')
        vehicle2_id = request.POST.get('vehicle2')
        vehicle1 = get_object_or_404(Details, pk=vehicle1_id)
        vehicle2 = get_object_or_404(Details, pk=vehicle2_id)
       
        context = {
            'vehicle1': vehicle1,
            'vehicle2': vehicle2,
           
        }
        return render(request, 'compare.html', context)
    else:
        vehicles = Vehicle.objects.all()
        context = {
            'vehicles': vehicles,
        }
        return render(request, 'compare.html', context)
