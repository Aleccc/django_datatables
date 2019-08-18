from django.views.generic import TemplateView
from django_datatables_view.base_datatable_view import BaseDatatableView

from event.models import Result


class ResultView(TemplateView):
    model = Result
    template_name = 'result.html'


class ResultDataTable(BaseDatatableView):
    model = Result
    columns = ['event.name', 'name', 'time', 'distance']
