"""
Thrown when a Savanna API call does not succeed.
"""

class Error:

    def __init__(self, code, info, message):
        self.code = code
        self.info = info
        self.message = message

    """
    The status code returned by the API.
    """
    @property
    def code(self):
        return self._code

    """
    Link to a web page providing more information about result of the API call.
    """
    @property
    def info(self):
        return self._info
    
    """
    Provides information about the result of the API call.
    """
    @property
    def message(self):
        return self._message
    """
    Initializes a new instance of the System.Exception class with a specified error message and a reference to
    the inner exception that is the cause of this exception.

    param name="message">The error message that explains the reason for the exception.</param>
    param name="Exception">The exception that is the cause of the current exception, or a null reference
    if no inner exception is specified.
    """
    @classmethod
    def error(self, message=None, Exception=None):
        return self