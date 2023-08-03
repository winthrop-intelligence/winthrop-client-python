"""module for PaginatedIterator class"""
class PaginatedIterator:
    """A simple iterator to mimic ActiveRecord's #find_each method

    Example:
    '''python
    for coach in PaginatedIterator(api_instance.get_coaches)(q:{first_name_eq: "Roy"}):
        print(coach)
    """

    def __init__(self, api_func, *args, **kwargs):
        self.api_func = api_func
        self.args = args
        self.kwargs = kwargs
        self.current_page = 1
        self.current_data = []

    def __call__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs
        return self

    def __iter__(self):
        return self

    def __next__(self):
        if not self.current_data:
            self.kwargs["page"] = self.current_page
            if not self.kwargs["page"]:
                raise StopIteration
            collection = self.api_func(*self.args, **self.kwargs)
            if not collection.data:
                raise StopIteration
            self.current_data = collection.data
            self.current_page = collection.meta.next_page
        return self.current_data.pop(0)
