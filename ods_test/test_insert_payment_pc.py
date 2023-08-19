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
from ods_client.models.insert_payment_pc import InsertPaymentPC  # noqa: E501
from ods_client.rest import ApiException


class TestInsertPaymentPC(unittest.TestCase):
    """InsertPaymentPC unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testInsertPaymentPC(self):
        """Test InsertPaymentPC"""
        # FIXME: construct object with mandatory attributes with example values
        # model = swagger_client.models.insert_payment_pc.InsertPaymentPC()  # noqa: E501

        api_instance = ods_client.HPPBindingApi()

        Document = ods_client.Q30Document(
            reservation_no = "reservation_no",
            payment_amount = "payment_amount"
        )
        
        Reservation = ods_client.Q30Reservation(
            [Document]
        )

        PaymentLine = ods_client.Q30PaymentLine(
            posting_date = "posting_date",
            payment_method_code = "payment_method_code",
            ext_document_no = "ext_document_no",
            reservation = Reservation,
            currency_code = "currency_code"
        )

        PaymentLines = ods_client.Q30PaymentLines([PaymentLine])

        TnsInsertPaymentPC = ods_client.TnsInsertPaymentPC(PaymentLines)

        body = ods_client.InsertPaymentPC(TnsInsertPaymentPC)

        try:
            # InsertPayment
            api_response = api_instance.insert_payment_pc(body)
        except ApiException as e:
            print("Exception when calling HPPBindingApi->insert_payment_pc: %s\n" % e)
            assert(False)        

if __name__ == '__main__':
    unittest.main()