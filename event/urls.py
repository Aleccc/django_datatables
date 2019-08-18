from django.urls import path

from .views import ResultDataTable


app_name = 'event'

urlpatterns = [
    path('', ResultDataTable.as_view(), name='resultdatatable'),
]