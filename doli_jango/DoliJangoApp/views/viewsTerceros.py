from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.urls import reverse
from django.forms import inlineformset_factory
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View
from ..models import Tercero
from ..forms import  TerceroForm
from ..models.choices import POBLACIONES_CHOICES
from django.db.models import F, Func, CharField
from django.http import JsonResponse
import json
from django.db.models import Q

import time

import sys

from django.views.generic import FormView, DetailView



class TerceroListView(ListView):
    model = Tercero
    template_name = 'tercero/tercero_list.html'
    context_object_name = 'tercero'
    
    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(
                Q(nombre__icontains=query) |
                Q(apellidos__icontains=query) |
                Q(dni__icontains=query) |
                Q(email__icontains=query)
            )
        return queryset

# Vista para crear un nuevo cliente
class TerceroCreateView(CreateView):
    model = Tercero
    form_class = TerceroForm
    template_name = 'tercero/tercero_form.html'
    success_url = reverse_lazy('tercero-list')
    
def crear_tercero(request):
    if request.method == 'POST':
        form = TerceroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tercero_list')
    else:
        form = TerceroForm()
    
   # Convierte el diccionario de provincias y poblaciones a un JSON string
    poblaciones_choices = json.dumps(POBLACIONES_CHOICES)

    context = {
       'form': form,
       'poblaciones_choices': poblaciones_choices,
    }
    
    return render(request, 'clientes/cliente_form.html', context)

# Vista para editar un cliente existente
class TerceroUpdateView(UpdateView):
    model = Tercero
    form_class = TerceroForm
    template_name = 'tercero/tercero_form.html'
    success_url = reverse_lazy('tercero-list')
    
    

# Vista para eliminar un cliente
class TerceroDeleteView(DeleteView):
    model = Tercero
    template_name = 'tercero/terceroconfirm_delete.html'
    success_url = reverse_lazy('tercero-list')