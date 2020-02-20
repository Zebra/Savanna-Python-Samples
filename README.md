Zebra Savanna Data Services Python Sample Code
==============================================

This sample code is meant to be used with the [Savanna Python SDK](https://github.com/Zebra/Savanna-Python-SDK).  It shows basic demos of the main Data Services APIs and how to use the native Python SDK to access them.  Primary use for the back end of web applications and data gathering for analytics in data science projects.

For more information on these APIs, go to [Developer.zebra.com/apis](https://developer.zebra.com/apis) or visit the [Forums](https://developer.zebra.com/forum/search?keys=&field_zebra_curated_tags_tid%5B%5D=273)



Requirements
--------

This sample is developed to run against Python3.

This sample requires the `jsonpickly` module to be installed. You can install it using the following command:
```
$> python3 -m pip install jsonpickle
```

Before running the sample you must edit the `application.py` file and enter your API key. To obtain an API key please read the instructions below in the API Key section. Once you have obtained a key from the Zebra Developer Portal, enter it on the line containing the following code: `SavannaAPI.APIKey = ""`



To Run the Sample
--------
```
python3 application.py
```




API Key
--------

To get an API key to work with these APIs, use the [Getting Started Guide](https://developer.zebra.com/gsg) and select the Barcode Intelligence product.  
