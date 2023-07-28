from rest_framework.pagination import PageNumberPagination

class SmallPagination(PageNumberPagination):
    page_size = 10
    page_query_param = 'page'

class MediumPagination(PageNumberPagination):
    page_size = 50

class LargePagination(PageNumberPagination):
    page_size = 100



