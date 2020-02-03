import http
from savanna.SavannaAPI import SavannaAPI
from urllib.error import URLError
import logging
import savanna.Rotation as rotation

"""
CreateBarcode --- Provides access to the Savanna barcode creation APIs.

@author Dbuhrsmith@zebra.com

"""


class CreateBarcode:

    # //TODO rotation.Normal.get() Does not work skipping problem for now will come back.
    @staticmethod
    def create(symbology, text, scale, rotation, includeText):
        """Generates a barcode from the text provided and returns a PNG image

        @param symbology The barcode symbology.
            @param text      The data or text to include in the generated barcode.
                             Usually an error will occur when the barcode symbology
                             cannot support the text provided. Different symbology
                             allow for numbers only, or alpha-numeric, or uppercase
                             alphabets, and some restrict characters. For example:
                             code39 only accepts numbers and uppercase letters.
            @param scale       Sets both the x-axis and the y-axis scaling factors. Must
                             be an integer &gt; 0. Use if you want default X &amp; Y,
                             just different size.
            @param rotate      Rotates the barcode in 90 degree increments.
            @param includeText Allows for the data included in the barcode to be printed
                             in human readable form with the barcode (usually printed
                             text under the linear barcode, this setting is ignored for
                             many 2D symbologies such as qrcode).
            @return A byte array containing the png-encoded image
            @throws HTTPError Thrown if there is an error calling the service

        """
        try:
            scale = 1
            includeText = False
            rotation = "N"
            return SavannaAPI.callServiceBytes("barcode/generate?symbology={}&text={}&scale={}&rotate={}&includeText={}"
                                        .format(symbology, text, scale, rotation, includeText))
        except URLError as error:
            logging.error(error)
            raise

    @staticmethod
    def create(symbology, text, scaleX, scaleY, rotation, includeText):
        """Generates a barcode from the text provided and returns a PNG image

        @param symbology The barcode symbology.
            @param text      The data or text to include in the generated barcode.
                             Usually an error will occur when the barcode symbology
                             cannot support the text provided. Different symbology
                             allow for numbers only, or alpha-numeric, or uppercase
                             alphabets, and some restrict characters. For example:
                             code39 only accepts numbers and uppercase letters.
            @param scaleX    Sets the x-axis. Must be an integer &gt; 0. Use with
                             scaleY, if using scale only, leave scaleX &amp; scaleY
                             blank. Allows proportional changes to the resulting
                             barcode, helpful with linear barcodes to make tall or
                             short.
            @param scaleY    Sets the y-axis scaling factors. Must be an integer &gt;
                             0. Use with scaleX.
            @param rotate    Rotates the barcode in 90 degree increments.
            @param includeText Allows for the data included in the barcode to be printed
                             in human readable form with the barcode (usually printed
                             text under the linear barcode, this setting is ignored for
                             many 2D symbologies such as qrcode).
            @return A byte array containing the png-encoded image
            @throws HTTPError Thrown if there is an error calling the service

        """
        try:
            return SavannaAPI.callServiceBytes("barcode/generate?symbology={}&text={}&scaleX={}&scaleY={}&rotate={}&includeText={}"
                                            .format(symbology, text, scaleX, scaleY, rotation, includeText))
        except URLError as error:
            logging.error(error)
            raise
