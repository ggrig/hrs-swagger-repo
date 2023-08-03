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
from swagger_client.models.confirm_invoice import ConfirmInvoice  # noqa: E501
from swagger_client.rest import ApiException

from pprint import pprint


class TestConfirmInvoice(unittest.TestCase):
    """ConfirmInvoice unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testConfirmInvoice(self):
        """Test ConfirmInvoice"""
        # FIXME: construct object with mandatory attributes with example values
        # model = swagger_client.models.confirm_invoice.ConfirmInvoice()  # noqa: E501
        # pass

        api_instance = swagger_client.HPPBindingApi()
        body = swagger_client.ConfirmInvoice() # ConfirmInvoice | 

        try:
            # InsertPayment
            api_response = api_instance.confirm_invoice(body)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling HPPBindingApi->confirm_invoice: %s\n" % e)
            assert(False)


if __name__ == '__main__':
    unittest.main()
