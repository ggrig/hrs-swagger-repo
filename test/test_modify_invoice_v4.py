# coding: utf-8

"""
    HPP

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import ods_client
from ods_client.models.modify_invoice_v4 import ModifyInvoiceV4  # noqa: E501
from ods_client.rest import ApiException

class TestModifyInvoiceV4(unittest.TestCase):
    """ModifyInvoiceV4 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testModifyInvoiceV4(self):
        """Test ModifyInvoiceV4"""
        # FIXME: construct object with mandatory attributes with example values
        # model = swagger_client.models.modify_invoice_v4.ModifyInvoiceV4()  # noqa: E501
        # pass

        api_instance = ods_client.HPPBindingApi()

        q22invoiceaddress = ods_client.Q22InvoiceAddress(
            address = "address",
            address2 = "address2",
            city = "city",
            customer_no = "customer_no",
            name = "name",
            name2 = "name2",
            post_code = "post_code",
            country_code = "country_code",
            correspondence_type = "correspondence_type",
            correspondence_address = "correspondence_address",
            accounting_contact = "accounting_contact"
        )

        q22positions = ods_client.Q22Positions(
            is_cancelled = "is_cancelled",
            case_no = "case_no",
            reservation_no = "reservation_no",
            position_no = 0,
            process_no = 0,
            number_of_nights = "string",
            number_of_rooms = 0,
            number_of_person = 0,
            number_of_breakfast = 0,
            room_price  = "room_price",
            reservation_date_from  = "reservation_date_from",
            reservation_date_to  = "reservation_date_to",
            breakfast_price  = "breakfast_price",
            deduction_type  = "deduction_type",
            reason_for_change  = "reason_for_change",
            room_type = 0,
            breakfast_approval_status = "breakfast_approval_status",
            non_comm = "non_comm"
        )
        positions_list = []
        positions_list.append(q22positions)

        q22_Invoice = ods_client.Q22Invoice(
            doc_no = "doc_no",
            is_cancelled = "is_cancelled",
            invoice_address = q22invoiceaddress,
            positions = positions_list
        )

        invoice_list = []
        invoice_list.append(q22_Invoice)

        q22_InvoiceList = ods_client.Q22InvoiceList(invoice_list)
        tns_modifyinvoicev4 = ods_client.TnsModifyInvoiceV4(q22_InvoiceList)
        body = ods_client.ModifyInvoiceV4Body(tns_modifyinvoicev4) # ModifyInvoiceV4Body | 

        try:
            # ModifyInvoiceV4
            api_response = api_instance.modify_invoice_v4(body)
        except ApiException as e:
            print("Exception when calling HPPBindingApi->modify_invoice_v4: %s\n" % e)
            assert(False)

if __name__ == '__main__':
    unittest.main()
