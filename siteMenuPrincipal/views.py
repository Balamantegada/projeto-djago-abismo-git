# Create your views here.
from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import FormView
from django.urls import reverse_lazy
from siteMenuPrincipal.models import PaginaInicial


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['NavBar'] = PaginaInicial.objects.order_by('-id').all()
        context['tituloPrincipal'] = PaginaInicial.objects.order_by('-id').all()
        context['segundaSessao'] = PaginaInicial.objects.order_by('-id').all()
        context['terceiraSessao'] = PaginaInicial.objects.order_by('-id').all()
        context['quartaSessao'] = PaginaInicial.objects.order_by('-id').all()
        context['quintaSessao'] = PaginaInicial.objects.order_by('-id').all()
        context['sextaSessao'] = PaginaInicial.objects.order_by('-id').all()
        context['setimaSessao'] = PaginaInicial.objects.order_by('-id').all()
        context['oitavaSessao'] = PaginaInicial.objects.order_by('-id').all()
        context['nonaSessao'] = PaginaInicial.objects.order_by('-id').all()
        context['Rodape'] = PaginaInicial.objects.order_by('-id').all()

        return context
