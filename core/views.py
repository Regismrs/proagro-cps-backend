from datetime import datetime
import math
from rest_framework import viewsets, generics, filters
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from django_filters import rest_framework as filters
from rest_framework import filters as drf_filters


from .models import ComunicadoCliente, Evento
from .serializers import ComunicadoClienteSerializer, ComunicadoSimpleSerializer,  EventoSerializer
from .filters import ComunicadoClientFilter


class ComunicadoClienteViewSet(viewsets.ModelViewSet):
    queryset = ComunicadoCliente.objects.all().order_by('id')
    serializer_class = ComunicadoClienteSerializer
    #authentication_classes = [ TokenAuthentication ]
    #permission_classes = [ IsAuthenticated ]


class ComunicadoClienteListView(generics.ListAPIView):
    queryset = ComunicadoCliente.objects.all()
    serializer_class = ComunicadoSimpleSerializer
    filter_backends = [filters.DjangoFilterBackend, drf_filters.OrderingFilter]
    filterset_class = ComunicadoClientFilter
    ordering_fields = ['id', 'nome', 'lavoura_data_colheita', 'inserted_at']

    def listEvento(self, request, *args, **kwargs):
        if (request.GET.get('evento__ne')):
            self.queryset = self.queryset.exclude(evento = 'evento__ne')


class EventoViewSet(viewsets.ModelViewSet):
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer

    def list(self, request, *args, **kwargs):
        queryset = Evento.objects.all()
        serializer_class = EventoSerializer(queryset, many=True)
        return Response(serializer_class.data)