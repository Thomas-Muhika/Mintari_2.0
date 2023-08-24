import django_tables2 as tables
from portal.models import RecordOrder


class RecordsTable(tables.Table):
    class Meta:
        model = RecordOrder