"""
Response object for UPC lookup
"""
class BarcodeData:

    def __init__(self, code, total, offset, items):
        self.code = code
        self.total = total
        self.offset = offset
        self.items = items
    
    """
    The status code returned by the API.
    """
    @property
    def code(self):
        return self._code

    """
    The total number of records matching the search criteria.
    """
    @property
    def total(self):
        return self._total
    
    """
    The Offset (page) of results.
    """
    @property
    def offset(self):
        return self._offset
    
    """
    Collection of items matching the UPC lookup query.
    """
    @property
    def items(self):
        return self._items