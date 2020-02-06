import http
from SavannaAPI import SavannaAPI
from urllib.error import URLError
import logging

"""
CreateBarcode --- Provides access to the Savanna barcode creation APIs.

@author Dbuhrsmith@zebra.com

"""

class FDARecall:

    @staticmethod
    def deviceSearch(search, limit = 1):

        """Returns medical device recall notices for a given description

        @param search A simple one word search string
        @param limit  Maximum number of records to return
        @return A JSONObject containing a result from the device recall search, if
            any
	    @throws HTTPError Thrown if there is an error calling the service

        """

        try:
            return SavannaAPI.callService("recalls/device/description?val={}&limit={}"
            .format(search, limit))
        except URLError as error:
            logging.error(error)
            raise

    @staticmethod
    def drugSearch(search, limit = 1):

        """Returns drug recall notices for a given description

        @param search A simple one word search string
        @param limit  Maximum number of records to return
        @return A JSONObject containing results from the drug recall search, if any
	    @throws HTTPError Thrown if there is an error calling the service

        """

        try:
            return SavannaAPI.callService("recalls/drug/description?val={}&limit={}"
            .format(search, limit))
        except URLError as error:
            logging.error(error)
            raise

    @staticmethod
    def foodUpc(upc, limit = 1):

        """Returns food recall notices for a given UPC code

        @param A valid UPC code for a food item
        @param limit Maximum number of records to return (maximum 99)
        @return A JSONObject containing a result from the food recall lookup, if any
	    @throws HTTPError Thrown if there is an error calling the service

        """

        try:
            return SavannaAPI.callService("recalls/food/upc?val={}&limit={}"
            .format(upc, limit))
        except URLError as error:
            logging.error(error)
            raise

    @staticmethod
    def drugUpc(upc, limit = 1):

        """Returns FDA drug recall notices for a UPC code

        @param upc Value
        @param limit Maximum number of records to return
        @return A JSONObject containing a result from the drug recall lookup, if any
	    @throws HTTPError Thrown if there is an error calling the service

        """

        try:
            return SavannaAPI.callService("recalls/drug/upc?val={}&limit={}"
            .format(upc, limit))
        except URLError as error:
            logging.error(error)
            raise