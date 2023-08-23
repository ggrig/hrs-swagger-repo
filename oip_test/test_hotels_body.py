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
from oip_client.models.hotels_body import HotelsBody  # noqa: E501
from oip_client.rest import ApiException
from pprint import pprint

class TestHotelsBody(unittest.TestCase):
    """HotelsBody unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testHotelsBody(self):
        print("""Test HotelsBody""")
        # FIXME: construct object with mandatory attributes with example values
        # model = swagger_client.models.hotels_body.HotelsBody()  # noqa: E501

        # Configure OAuth2 access token for authorization: oauth2
        configuration = oip_client.Configuration()

        # create an instance of the API class
        api_instance = oip_client.DefaultApi(oip_client.ApiClient(configuration))
        body = oip_client.HotelsBody(
            vat_registration_number = 'str',
            no_corrections = 'str',
            invoice_address_no = 'str',
            hotel_address_no = 'str',
            company_no = 'str',
            invoice_address_name = 'str',
            invoice_address_name2 = 'str',
            invoice_address_line1 = 'str',
            invoice_address_line2 = 'str',
            primary_contact_no = 'str',
            brand_no = 'str',
            brand_name = 'str',
            invoice_address_city = 'str',
            contract_status = 'str',
            contract_status_name = 'str',
            chain_no = 'str',
            chain_name = 'str',
            invoice_address_country_region_code = 'str',
            hotel_status = 'str',
            invoice_address_email = 'str',
            invoice_address_email_copy = 'str',
            invoice_address_fax_no = 'str',
            invoice_address_fax_no_copy = 'str',
            invoice_address_language_code = 'str',
            reason_code = 'str',
            no_sepa_core = 'str',
            reason_name = 'str',
            reason_date = 'str',
            phone_no = 'str',
            hrs_contact = 'str',
            invoioce_address_zip = 'str',
            ccpkn = 'str',
            cc_name = 'str',
            cc_valid_to = 'str',
            contact_person_first_name = 'str',
            contact_person_middle_name = 'str',
            contact_person_last_name = 'str',
            contact_person_email = 'str',
            contact_person_phone = 'str',
            contact_person_fax = 'str',
            hotel_address_name = 'str',
            hotel_address_country_region_code = 'str',
            hotel_address_language_code = 'str',
            hotel_address_name2 = 'str',
            hotel_address_line1 = 'str',
            hotel_address_line2 = 'str',
            hotel_address_city = 'str',
            hotel_address_zip = 'str',
            hotel_address_phone_no = 'str',
            hotel_address_fax_no = 'str',
            hotel_address_email = 'str',
            web_portal_enabled = True,
            correspondence_type = 'str',
            accounting_contact = 'str',
            deduction_type = 'str',
            tenant = 'str'            
        ) # HotelsBody | 

        try:
            # Create Booking Source
            api_response = api_instance.hotels_post(body)
            # pprint(api_response)
        except ApiException as e:
            print("Exception when calling DefaultApi->hotels_post: %s\n" % e)

if __name__ == '__main__':
    unittest.main()
