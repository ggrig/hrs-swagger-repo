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
from ods_client.models.insert_payment_v3 import InsertPaymentV3  # noqa: E501
from ods_client.rest import ApiException

class TestInsertPaymentV3(unittest.TestCase):
    """InsertPaymentV3 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testInsertPaymentV3(self):
        """Test InsertPaymentV3"""
        # FIXME: construct object with mandatory attributes with example values
        # model = swagger_client.models.insert_payment_v3.InsertPaymentV3()  # noqa: E501

        api_instance = ods_client.HPPBindingApi()

        q20document = ods_client.Q20Document(
            document_no = "document_no",
            document_type = "document_type",
            document_amount = "document_amount"
        )

        document_list = []
        document_list.append(q20document)
        q20documents = ods_client.Q20Documents(document_list)

        q20paymentline = ods_client.Q20PaymentLine(
            posting_date = "posting_date",
            payment_method_code = "payment_method_code",
            ext_document_no = "ext_document_no",
            documents = q20documents,
            currency_code = "currency_code",
            remaining_amount = "remaining_amount",
            fix_fee_amount = "fix_fee_amount",
            var_fee_amount = "var_fee_amount",
        )

        paymentline_list = []
        paymentline_list.append(q20paymentline)

        q20paymentlines = ods_client.Q20PaymentLines(payment_line = paymentline_list)
        tnsinsertpaymentv3 = ods_client.TnsInsertPaymentV3(q20paymentlines)

        body = ods_client.InsertPaymentV3(tnsinsertpaymentv3) # InsertPaymentV3 | 

        try:
            # InsertPayment
            api_response = api_instance.insert_payment_v3(body)
        except ApiException as e:
            print("Exception when calling HPPBindingApi->insert_payment_v3: %s\n" % e)
            assert(False)

if __name__ == '__main__':
    unittest.main()
