import io
import http.client
from urllib.error import HTTPError
import logging

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
    APIKey = "dquukdgDLgG4nZ0hTDL2lvdpleRkLsfM"

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
        headers = {'apikey': "dquukdgDLgG4nZ0hTDL2lvdpleRkLsfM", 'cache-control': "no-cache"}
        payload = "" 

        try:
            con = http.client.HTTPSConnection(SavannaAPI.host)
            con.request("GET", SavannaAPI.baseUrl + api, payload, headers)

            res = con.getresponse()
            status = res.status
            data = res.read()
            if(status != 200):
                logging.error("Request Status: "+ str(status))
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
