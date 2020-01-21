 """
 Describes issues encountered while invoking an API.
 """
class Fault:

    def __init__(self, faultString, detail):
        self.faultString = faultString
        self.detail = detail
    """
    The fault that occurred.
    """
    @property
    def faultString(self):
        return self.__faultString
    
    """
    Provides details about the results of the API call.
    """
    @property
    def detail(self):
        return self.__detail