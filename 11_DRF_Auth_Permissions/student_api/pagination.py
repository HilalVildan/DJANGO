from rest_framework.pagination import (
    PageNumberPagination,
    LimitOffsetPagination,
    CursorPagination
)

class CustomPageNumberPagination(PageNumberPagination):
    page_size = 10 #10tane kayit gelsin her sayfada
    page_query_param = 'sayfa' #link isminde page yerine sayfa yazabilirim. onu degistirmek icin kullanilir
    


class CustomLimitOffsetPagination(LimitOffsetPagination):
    default_limit =10
    limit_query_param = 'adet'
    offset_query_param = 'baslangic'
    max_limit = 20 #default limiti etkilemez. limit paremetresi icin max degeri ifade eder.


class CustomCursorPagination(CursorPagination):
    cursor_query_param = 'imlec'
    page_size = 10 
    # ordering = 'number'
    ordering = '-id' # önüne eksi koyunca ters siralaa demek