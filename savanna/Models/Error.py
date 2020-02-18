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
    
    @code.setter
    def code(self, code):
        self._code = code

    """
    Link to a web page providing more information about result of the API call.
    """
    @property
    def info(self):
        return self._info

    @info.setter
    def info(self, info):
        self._info = info
    
    """
    Provides information about the result of the API call.
    """
    @property
    def message(self):
        return self._message

    @message.setter
    def message(self, message):
        self._message = message
    """
    String version of the Error message formated for the console.
    """
    def __str__(self):
        errorString = "\nError Code: {}\nInfo: {}\nMessage:{}\n".format(self.code,self.info,self.message)
        return errorString