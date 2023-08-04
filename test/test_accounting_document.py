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
from oip_client.models.accounting_document import AccountingDocument  # noqa: E501
from oip_client.rest import ApiException

from pprint import pprint


class TestAccountingDocument(unittest.TestCase):
    """AccountingDocument unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testAccountingDocument(self):
        """Test AccountingDocument"""
        # FIXME: construct object with mandatory attributes with example values
        # model = swagger_client.models.accounting_document.AccountingDocument()  # noqa: E501
        # pass

        # Configure OAuth2 access token for authorization: oauth2
        configuration = oip_client.Configuration()
        configuration.access_token = 'YOUR_ACCESS_TOKEN'

        api_instance = oip_client.DefaultApi()
        body = oip_client.AccountingDocument() # AccountingDocument | 

        try:
            # InsertPayment
            api_response = api_instance.accountingdocuments_document_id_put(body, None)
            # api_response = api_instance.accountingdocuments_document_id_put_with_http_info(body, None)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling DefaultApi->accounting_document: %s\n" % e)
            assert(False)

if __name__ == '__main__':
    unittest.main()