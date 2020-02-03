import io
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

    baseUrl = "https;//api.zebra.com/v2/tools/"
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
        headers = {
            'Authorization': SavannaAPI.APIKey,
        }
        try:
            con = http.client.HTTPConnection(uri)
            con.request("GET", url, payload, headers)
            # except expression as identifier:
            try:
                in_ = io.BufferedIOBase(con.read())
            except io.BlockingIOError as error:
                in_ = io.BufferedIOBase(con.read())

            out = None

            buf = bytearray(1024)
            n = 0
            while (-1 != in_.read(buf)):
                out.io.BufferedIOBase.write(buf, 0, in_.read(buf))
                pass

            out.close()
            in_.close()

            response = io.BufferedIOBase.readinto(out)
            status = con.status()

        except e as error:
            traceback.print_exc()
        finally:
            con.close()
        if(status >= 400):
            except
        try:
            if(status <= 400)
            pass
        except HTTPError as error:
            logging(status)
        return response
