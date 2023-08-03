# coding: utf-8

"""
    HPP

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.models.modify_hotel_credit_card_info import ModifyHotelCreditCardInfo  # noqa: E501
from swagger_client.rest import ApiException

from pprint import pprint


class TestModifyHotelCreditCardInfo(unittest.TestCase):
    """ModifyHotelCreditCardInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testModifyHotelCreditCardInfo(self):
        """Test ModifyHotelCreditCardInfo"""
        # FIXME: construct object with mandatory attributes with example values
        # model = swagger_client.models.modify_hotel_credit_card_info.ModifyHotelCreditCardInfo()  # noqa: E501
        # pass

        api_instance = swagger_client.HPPBindingApi()
        body = swagger_client.ModifyHotelCreditCardInfo() # ModifyHotelCreditCardInfo | 

        try:
            # InsertPayment
            api_response = api_instance.modify_hotel_credit_card_info(body)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling HPPBindingApi->modify_hotel_credit_card_info: %s\n" % e)
            assert(False)

if __name__ == '__main__':
    unittest.main()
