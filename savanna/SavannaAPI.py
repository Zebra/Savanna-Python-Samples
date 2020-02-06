import io
import http.client
from urllib.error import HTTPError
import logging

"""
SavannaAPI --- Provides common functionality for acces to Savanna APIs.

@author Dbuhrsmith@zebra.com

"""


class SavannaAPI:

    baseUrl = "https://api.zebra.com/v2/tools"
    """
    Your Zebra Savanna application key
    """
    APIKey = None

    @staticmethod
    def callService(api):
        try:
            payload = SavannaAPI.callServiceBytes(api)
            return payload.decode("utf-8")
        except HTTPError as error:
            logging.error(error)
            raise

    @staticmethod
    def callServiceBytes(api):
        headers = {'Authorization': SavannaAPI.APIKey, 'cache-control': "no-cache"}
        payload = "" 

        try:
            con = http.client.HTTPSConnection(SavannaAPI.baseUrl)
            con.request("GET", api, payload, headers)

            res = con.getresponse()
            status = res.status
            if(status != 200):
                logging.error("Request Status: "+ str(status))
                raise
            data = res.read()

        except HTTPError as error:
            logging.error(HTTPError)

        try:
            if(status <= 400):
                pass

        except HTTPError as error:
            logging(status)

        finally:
            con.close()

        return data
