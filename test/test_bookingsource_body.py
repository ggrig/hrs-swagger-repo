# coding: utf-8

"""
    OIP API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import oip_client
from oip_client.models.bookingsource_body import BookingsourceBody  # noqa: E501
from oip_client.rest import ApiException
from pprint import pprint

class TestBookingsourceBody(unittest.TestCase):
    """BookingsourceBody unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testBookingsourceBody(self):
        """Test BookingsourceBody"""
        # FIXME: construct object with mandatory attributes with example values
        # model = oip_client.models.bookingsource_body.BookingsourceBody()  # noqa: E501
        pass


        # Configure OAuth2 access token for authorization: oauth2
        configuration = oip_client.Configuration()
        configuration.access_token = 'YOUR_ACCESS_TOKEN'

        # create an instance of the API class
        api_instance = oip_client.DefaultApi(oip_client.ApiClient(configuration))
        body = oip_client.BookingsourceBody() # BookingsourceBody | 

        try:
            # Create Booking Source
            api_response = api_instance.booking_source_post(body)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling DefaultApi->booking_source_post: %s\n" % e)


if __name__ == '__main__':
    unittest.main()