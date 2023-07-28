from rest_framework.filters import SearchFilter, OrderingFilter

class YorumFilter(OrderingFilter):
    ordering_fields = ['yazi_id', 'yazar']