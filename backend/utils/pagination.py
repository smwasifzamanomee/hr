from rest_framework.pagination import PageNumberPagination



class CustomPageNumberPagination(PageNumberPagination): 
    page_size = 50 
    page_size_query_param = 'page_size' 
    max_page_size = 100

    def get_page_size(self, request):
        """
        Return the page size.
        """
        if self.page_size_query_param:
            try:
                page_size = int(request.query_params.get(
                    self.page_size_query_param, self.page_size))
                if page_size < 1:
                    raise ValueError
                return page_size
            except (TypeError, ValueError):
                pass

        return self.page_size