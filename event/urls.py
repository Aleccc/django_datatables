from django.urls import path

from .views import ResultView, ResultDataTable


app_name = 'event'

urlpatterns = [
    path('', ResultView.as_view(), name='result'),
    path('data/', ResultDataTable.as_view(), name='resultdatatable'),
]