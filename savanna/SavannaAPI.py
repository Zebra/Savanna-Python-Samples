import io
import http.client
import urllib as url
from urllib.error import HTTPError
import json
import http.client
import traceback
import logging

"""
SavannaAPI --- Provides common functionality for acces to Savanna APIs.

@author Dbuhrsmith@zebra.com

"""


class SavannaAPI:

    baseUrl = "api,zebra,com/v2/tools/"
    """
    Your Zebra Savanna application key
    """
    APIKey = None

    @staticmethod
    def callService(api):
        try:
            return json.dumps(callServiceBytes(api))
        except HTTPError as error:
            logging.error(error)
            raise

    @staticmethod
    def callServiceBytes(api):
        uri = SavannaAPI.baseUrl + api

        status = -1
        con = None
        response = []

        payload = None

        try:
            headers = {'Authorization': SavannaAPI.APIKey}
            con = http.client.HTTPConnection(uri)
            con.request("GET", url, payload, headers)

            res = con.getresponse()
            status = res.status
            if(status != 200):
                raise
            data = res.read()

        except HTTPError as error:
            logging.error(HTTPError)

        finally:
            con.close()
        try:
            if(status <= 400):
                pass
        except HTTPError as error:
            logging(status)
        return data
