from django_filters import FilterSet, AllValuesFilter
from django_filters import DateTimeFilter, NumberFilter
from .models import ComunicadoCliente

class ComunicadoClientFilter(FilterSet):
    data_cadastro__gte = DateTimeFilter(field_name='inserted_at', lookup_expr='gte')
    data_cadastro__gt = DateTimeFilter(field_name='inserted_at', lookup_expr='gt')
    data_cadastro__lte = DateTimeFilter(field_name='inserted_at', lookup_expr='lte')
    data_cadastro__lt = DateTimeFilter(field_name='inserted_at', lookup_expr='lt')
    data_cadastro = DateTimeFilter(field_name='inserted_at', lookup_expr='date')
    data_colheita__gte = DateTimeFilter(field_name='lavoura_data_colheita', lookup_expr='gte')
    data_colheita__gt = DateTimeFilter(field_name='lavoura_data_colheita', lookup_expr='gt')
    data_colheita__lte = DateTimeFilter(field_name='lavoura_data_colheita', lookup_expr='lte')
    data_colheita__lt = DateTimeFilter(field_name='lavoura_data_colheita', lookup_expr='lt')
    data_colheita = DateTimeFilter(field_name='lavoura_data_colheita', lookup_expr='date')
    evento = NumberFilter(field_name='evento', lookup_expr='exact')
    evento__ne = NumberFilter(field_name='evento', exclude=True)
    id__ne = NumberFilter(field_name='id', exclude=True)
 
    class Meta:
        model = ComunicadoCliente
        fields = {
            'lavoura_data_colheita',
            'inserted_at',
            'evento'
        }