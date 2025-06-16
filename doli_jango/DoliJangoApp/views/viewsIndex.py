from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.urls import reverse
from django.forms import inlineformset_factory
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View
from django.db.models import F, Func, CharField
from django.http import JsonResponse
import json
from django.db.models import Q
import time
import sys
from django.views.generic import FormView, DetailView

# Create your views here.

@login_required
def index(request):
    return render(request,'index.html',context={'sepal_length':3,'sepal_width':2,'petal_length':2,'petal_width':2,'class':"Iris Setosa"},)

class Unaccent(Func):
    function = 'UNACCENT'
    output_field = CharField()