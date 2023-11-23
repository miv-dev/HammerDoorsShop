from django.db.models import Q
from rest_framework import viewsets, filters, status
from rest_framework.decorators import api_view, action
from rest_framework.response import Response

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


    def filter_doors(self):
        queryset = Door.objects.all()

        title = self.request.query_params.get('title')
        desc = self.request.query_params.get('description')
        if title is not None and desc is not None:
            queryset = queryset.filter(Q(title__startswith=title), Q(description__startswith=desc))
        return queryset
    
    @action(detail=False, methods=['get'], url_path='filter')
    def filter_doors(self, request):
        queryset = Door.objects.filter(
            Q(price__gte=1000) & ~Q(price__gte=2400) | Q(branch='1')
        )
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['post'])
    def add_product(self, request):
        serializer = DoorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class BranchViewSet(viewsets.ModelViewSet):
    serializer_class = BranchSerializer
    queryset = Branch.objects.all()

    def get_queryset(self):
        queryset = Branch.objects.all()
        branch_id = self.kwargs['pk']
        item = queryset.filter(pk=branch_id)
        return item
