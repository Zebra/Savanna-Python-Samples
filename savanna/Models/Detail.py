"""
Provides details about the results of an API call.
"""

class Detail:

    def __init__(self, errorcode):
        self.errorcode = errorcode

    """
    The error code encountered while invoking the API.
    """
    @property
    def errorcode(self):
        return self._errorcode