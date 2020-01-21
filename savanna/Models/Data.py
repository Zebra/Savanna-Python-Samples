"""
Item matching a UPC lookup query
"""

class Data:

    def __init__(self, EAN, title, description, images, offers, 
    asin, isbn, publisher, upc, brand, model, color, size, dimension,
    weight, currency, lowestRecordedPrice, highestRecordedPrice, elid):
        self.EAN = EAN
        self.title = title
        self.description = description
        self.images = images
        self.offers = offers
        self.asin = asin
        self.isbn = isbn
        self.publisher = publisher
        self.upc = upc
        self.brand = brand
        self.model = model
        self.color = color
        self.size = size
        self.dimension = dimension
        self.weight = weight
        self.currency = currency
        self.lowestRecordedPrice = lowestRecordedPrice
        self.highestRecordedPrice = highestRecordedPrice
        self.elid = elid
    
    """
    EAN-13, 13-digit European Article Number (aka. GTIN-13). This is the unique number we used to identify each
    item in our database. If it starts with 0, the rest 12-digit is the UPC (aka. UPC-A, GTIN-12), ex.
    0885909456017.
    """
    @property
    def EAN(self):
        return self.__EAN

    """
    Item title
    """
    @property
    def title(self):
        return self.__title
    
    """
    Item description with length &lt; 515.
    """
    @property
    def description(self):
        return self.__description
    
    """
    Collection of image urls.
    """
    @property
    def images(self):
        return self.__images

    """
    Offers for item provided by merchants.
    """
    @property
    def offers(self):
        return self.__offers

    """
    Amazon Standard Identification Number (ASIN) is a 10-character alphanumeric unique identifier assigned by
    Amazon.com and its partners for product identification within the Amazon organization.
    """
    @property
    def asin(self):
        return self.__asin

    """
    International Standard Book Numbers (ISBN) are numeric commercial book identifiers which are intended to be
    unique. An ISBN is assigned to each separate edition and variation (except reprintings) of a publication.
    """
    @property
    def isbn(self):
        return self.__isbn

    """
    Publisher name
    """
    @property
    def publisher(self):
        return self.__publisher

    """
    UPC-A, 12-digit Universal Product Code (aka. GTIN-12). If item’s EAN does not start with 0, there is no
    corresponding UPC-A code, ex. 6009705662678.
    """
    @property
    def upc(self):
        return self.__upc

    """
    Brand name or manufacturer name with length &lt; 64.
    """
    @property
    def brand(self):
        return self.__brand

    """
    Item model number with length &lt; 32.
    """
    @property
    def model(self):
        return self.__model

    """
    Item color with length &lt; 32, ex. for clothing, shoes.
    """
    @property
    def color(self):
        return self.__color

    """
    Item size with length &lt; 32, ex. for clothing, shoes.
    """
    @property
    def size(self):
        return self.__size

    """
    Item model number with length &lt; 32.
    """
    @property
    def dimension(self):
        return self.__dimension

    """
    Item weight with length &lt; 16.
    """
    @property
    def weight(self):
        return self.__weight

    """
    Currency of the <see cref="lowestRecordedPrice"/>. Can be "USD", "CAD", "EUR", "GBP", "SEK". Default ""
    means "USD".
    """
    @property
    def currency(self):
        return self.__currency

    """
    Lowest historical price of the item since tracked by our system. Not available for books.
    """
    @property
    def lowestRecordedPrice(self):
        return self.__lowestRecordedPrice

    """
    Highest historical price of the item since tracked by our system. Not available for books.   
    """
    @property
    def highestRecordedPrice(self):
        return self.__highestRecordedPrice

    """
    eBay Listing ID, aka. item ID or item number. Item ID is 9 to 12 digits in length. If item is found on
    eBay.com, you can simply locate the item by http://www.ebay.com/itm/[eLID].
    """
    @property
    def elid(self):
        return self.__elid
    
