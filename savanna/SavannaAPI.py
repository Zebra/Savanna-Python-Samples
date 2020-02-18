import io
import http.client
from urllib.error import HTTPError
from savanna.Models.Error import Error
import logging
import jsonpickle

"""
SavannaAPI --- Provides common functionality for acces to Savanna APIs.

@author Dbuhrsmith@zebra.com

"""


class SavannaAPI:
    host = "api.zebra.com"
    baseUrl = "https://" + host + "/v2/tools/"
    """
    Your Zebra Savanna application key
    """
    APIKey = ""

    @staticmethod
    def callService(api):
        try:
            payload = SavannaAPI.callServiceBytes(api)
            print(payload.decode("utf-8"))
        except HTTPError as error:
            logging.error(error)
            raise

    @staticmethod
    def callServiceBytes(api):
        headers = {'apikey': SavannaAPI.APIKey, 'cache-control': "no-cache"}
        payload = None 

        try:
            con = http.client.HTTPSConnection(SavannaAPI.host)
            con.request("GET", SavannaAPI.baseUrl + api, payload, headers)

            res = con.getresponse()
            status = res.status
            data = res.read()
            if(status != 200 and status is not None):
                error = SavannaAPI.throwError(status, data)
                raise 

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

    @staticmethod
    def throwError(status, data):
        thawed = jsonpickle.decode(data)
        Error.code == thawed.code
        Error.info == thawed.info
        Error.message == thawed.message