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
    def deviceSearch(search):

        """Returns medical device recall notices for a given description

        @param search A simple one word search string    
        @return A JSONObject containing a result from the device recall search, if
            any
	    @throws HTTPError Thrown if there is an error calling the service

        """

        try:
            return FDARecall.deviceSearch_limit(search, 1)
        except URLError as error:
            logging.error(error)
            raise

    @staticmethod
    def deviceSearch_limit(search, limit):

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
    def drugSearch(search):

        """Returns drug recall notices for a given description

        @param search A simple one word search string
        @return A JSONObject containing results from the drug recall search, if any
	    @throws HTTPError Thrown if there is an error calling the service

        """

        try:
            return FDARecall.drugSearch_limit(search, 1)
        except URLError as error:
            logging.error(error)
            raise

    @staticmethod
    def drugSearch_limit(search, limit):

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
    def foodUpc(upc):

        """Returns food recall notices for a given UPC code

        @param A valid UPC code for a food item
        @return A JSONObject containing a result from the food recall lookup, if any
	    @throws HTTPError Thrown if there is an error calling the service

        """

        try:
            return FDARecall.foodUpc_limit(upc, 1)
        except URLError as error:
            logging.error(error)
            raise

    @staticmethod
    def foodUpc_limit(upc, limit):

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
    def drugUpc(upc):

        """Returns FDA drug recall notices for a UPC code

        @param upc Value
        @return A JSONObject containing a result from the drug recall lookup, if any
	    @throws HTTPError Thrown if there is an error calling the service

        """

        try:
            return FDARecall.drugUpc_upc_limit(upc, 1)
        except URLError as error:
            logging.error(error)
            raise

    @staticmethod
    def drugUpc_limit(upc, limit):

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