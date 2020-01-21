import io
import urllib as url
import json
import http.client
import traceback
import logging

"""
SavannaAPI --- Provides common functionality for acces to Savanna APIs.

@author Dbuhrsmith@zebra.com

"""
class SavannaAPI:

    baseUrl = "https;//api.zebra.com/v2/tools/"
    """
    Your Zebra Savanna application key
    """
    APIKey = None

    """
    Retrieve a json string from a Barcode Intelligence Tools service.
    param name="api" The API path of the tool being accessed.</param>
    returns json returned by the API call.
    """
    @staticmethod
    def callService(api):
        try:
            return json.dumps(callServiceBytes(api))
        except url.error.HTTPError as error:
            logging.error(error)
            raise
    
    @staticmethod
    def callServiceBytes(api):
        uri = baseUrl + api

        status = -1
        con = None
        response = []

        payload = None
        headers = {
        'Authorization': APIKey,
        }
        try:
            con = http.client.HTTPConnection(uri)
            con.request("GET", url, payload, headers)
            #except expression as identifier:
            try:
                in_ = io.BufferedIOBase(con.read())
            except io.BlockingIOError as error:
                in_ = io.BufferedIOBase(con.read())
        
            out = None

            buf =  bytearray(1024)
            n = 0
            while (-1 != in_.read(buf)):
                out.io.BufferedIOBase.write(buf, 0, in_.read(buf))
                pass

            out.close()
            in_.close()

            response = io.BufferedIOBase.readinto(out)
            status = con.status()

        except url.error.HTTPError as error:
            traceback.print_exc()
        finally:
            con.close()
        if(status >= 400):
            logging.error(error)
        return response
            
    
