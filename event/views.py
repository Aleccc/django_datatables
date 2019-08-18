from django_datatables_view.base_datatable_view import BaseDatatableView

from event.models import Result


class ResultDataTable(BaseDatatableView):
    model = Result
    columns = ['name', 'time', 'distance']
