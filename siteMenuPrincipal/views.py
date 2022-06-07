# Create your views here.
from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import FormView
from django.urls import reverse_lazy
from siteMenuPrincipal.models import ParteInicial, BarradeNavegação, SegundaSessão, TerceiraSessão, QuartaSessão, \
    QuintaSessão, SextaSessão, SetimaSessão, OitavaSessão, NonaSessão, Rodapé


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['NavBar'] = BarradeNavegação.objects.order_by('-id').all()
        context['tituloPrincipal'] = ParteInicial.objects.order_by('-id').all()
        context['segundaSessao'] = SegundaSessão.objects.order_by('-id').all()
        context['terceiraSessao'] = TerceiraSessão.objects.order_by('-id').all()
        context['quartaSessao'] = QuartaSessão.objects.order_by('-id').all()
        context['quintaSessao'] = QuintaSessão.objects.order_by('-id').all()
        context['sextaSessao'] = SextaSessão.objects.order_by('-id').all()
        context['setimaSessao'] = SetimaSessão.objects.order_by('-id').all()
        context['oitavaSessao'] = OitavaSessão.objects.order_by('-id').all()
        context['nonaSessao'] = NonaSessão.objects.order_by('-id').all()
        context['Rodape'] = Rodapé.objects.order_by('-id').all()

        return context
