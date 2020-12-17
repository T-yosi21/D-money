from django.shortcuts import render
from django.views import generic
from django.views.generic import TemplateView, DetailView
from django.views.generic.list import MultipleObjectMixin
from .models import Fstatement, Company


class IndexView(TemplateView):
    template_name = 'finchart/index.html'

    def get_context_data(self, **kwargs):
        fstatement_list = Fstatement.objects.all().order_by('company')
        params = {
            'fstatement_list': fstatement_list,
        }
        return params


class CompanyView(DetailView, MultipleObjectMixin):
    model = Company
    paginate_by = 4

    def get_context_data(self, **kwargs):
        company_name = kwargs['object'].name
        fstatement_list = Fstatement.objects.filter(
            company=kwargs['object']).order_by('-fiscal_year')
        params = {
            'company_name': company_name,
            'fstatement_list': fstatement_list,
        }
        return params


class fstatementView(DetailView):
    model = Fstatement

# Create your views here.
