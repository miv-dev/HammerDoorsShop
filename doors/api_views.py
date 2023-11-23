from django.db.models import Q
from rest_framework import viewsets, filters
from rest_framework.decorators import api_view, action

from .paginations import ResultsSetPagination
from .serializers import DoorSerializer, BranchSerializer
from .models import Door, Branch


class DoorViewSet(viewsets.ModelViewSet):
    serializer_class = DoorSerializer
    queryset = Door.objects.all()
    pagination_class = ResultsSetPagination
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['title', 'description']
    ordering_fields = ['price', 'popular']

    search_fields = ['title', 'description']

    def get_queryset(self):
        queryset = Door.objects.all()

        title = self.request.query_params.get('title')
        desc = self.request.query_params.get('description')
        if title is not None and desc is not None:
            queryset = queryset.filter(Q(title__startswith=title), Q(description__startswith=desc))
        return queryset
    


class BranchViewSet(viewsets.ModelViewSet):
    serializer_class = BranchSerializer
    queryset = Branch.objects.all()

    def get_queryset(self):
        queryset = Branch.objects.all()
        branch_id = self.kwargs['pk']
        item = queryset.filter(pk=branch_id)
        return item
