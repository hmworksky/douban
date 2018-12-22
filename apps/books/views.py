import logging
from rest_framework.generics import mixins
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from .models import Books, BookCategory
from .serializers import BooksSerializer, BookCategorySerializer
from .filters import BooksFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter

# Create your views here.


class BooksPagination(PageNumberPagination):
    page_size = 10
    page_query_param = 'p'
    max_page_size = 20


class BooksViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
        书籍分页、排序、搜索
    """
    queryset = Books.objects.all()
    serializer_class = BooksSerializer
    pagination_class = BooksPagination
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filter_class = BooksFilter
    ordering_fields = ("price", "add_time")
    search_fields = ("name", "is_new", "is_hot", "category_id", "author_id", "publish_information_id")
    logging.error(list(queryset))


class CategoryViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    list:
        书籍分类列表
    """
    queryset = BookCategory.objects.all()
    serializer_class = BookCategorySerializer


