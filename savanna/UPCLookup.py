import http
from SavannaAPI import SavannaAPI
import urllib as url
import logging
from Rotation import Rotation as rotation

"""
UPCLookup --- Provides access to the Savanna UPC Lookup API.

@author Dbuhrsmith@zebra.com

"""

class UPCLookup:

    @staticmethod
    def lookup(upc):
        """Retrieves product information in JSON format for a provided UPC code

        @param upc UPC Code
	    @return A JSONObject containing product information for the provided UPC
	    @throws HttpRetryException Thrown if there is an error calling the service

        """
        try:
            return SavannaAPI.callService("barcode/lookup?upc=" + upc)
        except urllib.error as error:
            logging.error(error)
            raise