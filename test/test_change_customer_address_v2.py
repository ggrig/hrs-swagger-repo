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
from ods_client.models.change_customer_address_v2 import ChangeCustomerAddressV2  # noqa: E501
from ods_client.rest import ApiException

from pprint import pprint


class TestChangeCustomerAddressV2(unittest.TestCase):
    """ChangeCustomerAddressV2 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testChangeCustomerAddressV2(self):
        """Test ChangeCustomerAddressV2"""
        # FIXME: construct object with mandatory attributes with example values
        # model = swagger_client.models.change_customer_address_v2.ChangeCustomerAddressV2()  # noqa: E501

        api_instance = ods_client.HPPBindingApi()

        q14customer = ods_client.Q14Customer(
            customer_no = "string",
            name = "string",
            name2 = "string",
            address = "string",
            address2 = "string",
            city = "string",
            post_code = "string",
            country_region = "string",
            contact = "string",
            phone = "string",
            correspondence_type = "string",
            e_mail = "string",
            fax = "string",
            e_mail_copy = "string",
            fax_copy = "string",
            webportal_registered = "string",
        )

        customer_list = []
        customer_list.append(q14customer)

        q14customerlist = ods_client.Q14CustomerList(customer_list)

        tnschangecustomeraddressv2 = ods_client.TnsChangeCustomerAddressV2(q14customerlist)

        body = ods_client.ChangeCustomerAddressV2Body(tnschangecustomeraddressv2)

        try:
            # InsertPayment
            api_response = api_instance.change_customer_address_v2(body)
        except ApiException as e:
            print("Exception when calling HPPBindingApi->change_invoice_address: %s\n" % e)
            assert(False)

if __name__ == '__main__':
    unittest.main()
