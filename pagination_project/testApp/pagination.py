from rest_framework.pagination import PageNumberPagination,LimitOffsetPagination,CursorPagination
class MyPagination(PageNumberPagination):
    page_size=5
    page_query_param='mypage'# default is page
    page_size_query_param='num'
    max_page_size=15
    last_page_strings=('endpage',)# default is ('last',)

class MyPagination2(LimitOffsetPagination):
    default_limit=15
    limit_query_param='mylimit'
    offset_query_param='myoffset'
    max_limit=20

class MyPagination3(CursorPagination):
    ordering='esal'
    page_size=5
