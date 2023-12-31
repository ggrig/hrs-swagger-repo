# coding: utf-8

"""
    HPP-V2

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import ods_client
from ods_client.models.confirm_invoice import ConfirmInvoice  # noqa: E501
from ods_client.rest import ApiException


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

        api_instance = ods_client.HPPBindingApi()

        q24invoice = ods_client.Q24Invoice(
            case_no = "string"
        )

        invoice_list = []
        invoice_list.append(q24invoice)

        q24invoicelist = ods_client.Q24InvoiceList(invoice_list)

        tnsconfirminvoice = ods_client.TnsConfirmInvoice(q24invoicelist)

        body = ods_client.ConfirmInvoice(tnsconfirminvoice)

        try:
            # InsertPayment
            api_response = api_instance.confirm_invoice(body)
        except ApiException as e:
            print("Exception when calling HPPBindingApi->confirm_invoice: %s\n" % e)
            assert(False)

if __name__ == '__main__':
    unittest.main()
