# coding: utf-8

# flake8: noqa

"""
    HPP

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

# import apis into sdk package
from swagger_client.api.hpp_binding_api import HPPBindingApi
# import ApiClient
from swagger_client.api_client import ApiClient
from swagger_client.configuration import Configuration
# import models into sdk package
from swagger_client.models.all_of_change_contact_information_change_contact_information import AllOfChangeContactInformationChangeContactInformation
from swagger_client.models.all_of_change_contact_information_result_change_contact_information_result import AllOfChangeContactInformationResultChangeContactInformationResult
from swagger_client.models.all_of_change_customer_address_change_customer_address import AllOfChangeCustomerAddressChangeCustomerAddress
from swagger_client.models.all_of_change_customer_address_result_change_customer_address_result import AllOfChangeCustomerAddressResultChangeCustomerAddressResult
from swagger_client.models.all_of_change_customer_address_v2_change_customer_address_v2 import AllOfChangeCustomerAddressV2ChangeCustomerAddressV2
from swagger_client.models.all_of_change_customer_address_v2_result_change_customer_address_v2_result import AllOfChangeCustomerAddressV2ResultChangeCustomerAddressV2Result
from swagger_client.models.all_of_change_invoice_address_change_invoice_address import AllOfChangeInvoiceAddressChangeInvoiceAddress
from swagger_client.models.all_of_change_invoice_address_result_change_invoice_address_result import AllOfChangeInvoiceAddressResultChangeInvoiceAddressResult
from swagger_client.models.all_of_confirm_invoice_confirm_invoice import AllOfConfirmInvoiceConfirmInvoice
from swagger_client.models.all_of_confirm_invoice_result_confirm_invoice_result import AllOfConfirmInvoiceResultConfirmInvoiceResult
from swagger_client.models.all_of_insert_payment_insert_payment import AllOfInsertPaymentInsertPayment
from swagger_client.models.all_of_insert_payment_result_insert_payment_result import AllOfInsertPaymentResultInsertPaymentResult
from swagger_client.models.all_of_insert_payment_v2_insert_payment_v2 import AllOfInsertPaymentV2InsertPaymentV2
from swagger_client.models.all_of_insert_payment_v2_result_insert_payment_v2_result import AllOfInsertPaymentV2ResultInsertPaymentV2Result
from swagger_client.models.all_of_insert_payment_v3_insert_payment_v3 import AllOfInsertPaymentV3InsertPaymentV3
from swagger_client.models.all_of_insert_payment_v3_result_insert_payment_v3_result import AllOfInsertPaymentV3ResultInsertPaymentV3Result
from swagger_client.models.all_of_modify_hotel_bank_account_info_modify_hotel_bank_account_info import AllOfModifyHotelBankAccountInfoModifyHotelBankAccountInfo
from swagger_client.models.all_of_modify_hotel_bank_account_info_result_modify_hotel_bank_account_info_result import AllOfModifyHotelBankAccountInfoResultModifyHotelBankAccountInfoResult
from swagger_client.models.all_of_modify_hotel_credit_card_info_modify_hotel_credit_card_info import AllOfModifyHotelCreditCardInfoModifyHotelCreditCardInfo
from swagger_client.models.all_of_modify_hotel_credit_card_info_result_modify_hotel_credit_card_info_result import AllOfModifyHotelCreditCardInfoResultModifyHotelCreditCardInfoResult
from swagger_client.models.all_of_modify_invoice_modify_invoice import AllOfModifyInvoiceModifyInvoice
from swagger_client.models.all_of_modify_invoice_result_modify_invoice_result import AllOfModifyInvoiceResultModifyInvoiceResult
from swagger_client.models.all_of_modify_invoice_v2_modify_invoice_v2 import AllOfModifyInvoiceV2ModifyInvoiceV2
from swagger_client.models.all_of_modify_invoice_v2_result_modify_invoice_v2_result import AllOfModifyInvoiceV2ResultModifyInvoiceV2Result
from swagger_client.models.all_of_modify_invoice_v3_modify_invoice_v3 import AllOfModifyInvoiceV3ModifyInvoiceV3
from swagger_client.models.all_of_modify_invoice_v3_result_modify_invoice_v3_result import AllOfModifyInvoiceV3ResultModifyInvoiceV3Result
from swagger_client.models.all_of_modify_invoice_v4_modify_invoice_v4 import AllOfModifyInvoiceV4ModifyInvoiceV4
from swagger_client.models.all_of_modify_invoice_v4_result_modify_invoice_v4_result import AllOfModifyInvoiceV4ResultModifyInvoiceV4Result
from swagger_client.models.all_ofq10_invoice_invoice_address import AllOfq10InvoiceInvoiceAddress
from swagger_client.models.all_ofq12_payment_line_documents import AllOfq12PaymentLineDocuments
from swagger_client.models.all_ofq16_invoice_invoice_address import AllOfq16InvoiceInvoiceAddress
from swagger_client.models.all_ofq18_invoice_invoice_address import AllOfq18InvoiceInvoiceAddress
from swagger_client.models.all_ofq20_payment_line_documents import AllOfq20PaymentLineDocuments
from swagger_client.models.all_ofq22_invoice_invoice_address import AllOfq22InvoiceInvoiceAddress
from swagger_client.models.all_ofq8_payment_line_documents import AllOfq8PaymentLineDocuments
from swagger_client.models.all_oftns_change_contact_information_contact_information import AllOftnsChangeContactInformationContactInformation
from swagger_client.models.all_oftns_change_contact_information_result_contact_information import AllOftnsChangeContactInformationResultContactInformation
from swagger_client.models.all_oftns_change_customer_address_customer_address import AllOftnsChangeCustomerAddressCustomerAddress
from swagger_client.models.all_oftns_change_customer_address_result_customer_address import AllOftnsChangeCustomerAddressResultCustomerAddress
from swagger_client.models.all_oftns_change_customer_address_v2_customer_address import AllOftnsChangeCustomerAddressV2CustomerAddress
from swagger_client.models.all_oftns_change_customer_address_v2_result_customer_address import AllOftnsChangeCustomerAddressV2ResultCustomerAddress
from swagger_client.models.all_oftns_change_invoice_address_invoice_address import AllOftnsChangeInvoiceAddressInvoiceAddress
from swagger_client.models.all_oftns_change_invoice_address_result_invoice_address import AllOftnsChangeInvoiceAddressResultInvoiceAddress
from swagger_client.models.all_oftns_confirm_invoice_confirm_invoice import AllOftnsConfirmInvoiceConfirmInvoice
from swagger_client.models.all_oftns_confirm_invoice_result_confirm_invoice import AllOftnsConfirmInvoiceResultConfirmInvoice
from swagger_client.models.all_oftns_insert_payment_insert_payment import AllOftnsInsertPaymentInsertPayment
from swagger_client.models.all_oftns_insert_payment_result_insert_payment import AllOftnsInsertPaymentResultInsertPayment
from swagger_client.models.all_oftns_insert_payment_v2_insert_payment import AllOftnsInsertPaymentV2InsertPayment
from swagger_client.models.all_oftns_insert_payment_v2_result_insert_payment import AllOftnsInsertPaymentV2ResultInsertPayment
from swagger_client.models.all_oftns_insert_payment_v3_insert_payment import AllOftnsInsertPaymentV3InsertPayment
from swagger_client.models.all_oftns_insert_payment_v3_result_insert_payment import AllOftnsInsertPaymentV3ResultInsertPayment
from swagger_client.models.all_oftns_modify_hotel_bank_account_info_modify_bank_acc_info import AllOftnsModifyHotelBankAccountInfoModifyBankAccInfo
from swagger_client.models.all_oftns_modify_hotel_bank_account_info_result_modify_bank_acc_info import AllOftnsModifyHotelBankAccountInfoResultModifyBankAccInfo
from swagger_client.models.all_oftns_modify_hotel_credit_card_info_modify_credit_card_info import AllOftnsModifyHotelCreditCardInfoModifyCreditCardInfo
from swagger_client.models.all_oftns_modify_hotel_credit_card_info_result_modify_credit_card_info import AllOftnsModifyHotelCreditCardInfoResultModifyCreditCardInfo
from swagger_client.models.all_oftns_modify_invoice_modify_invoice import AllOftnsModifyInvoiceModifyInvoice
from swagger_client.models.all_oftns_modify_invoice_result_modify_invoice import AllOftnsModifyInvoiceResultModifyInvoice
from swagger_client.models.all_oftns_modify_invoice_v2_modify_invoice import AllOftnsModifyInvoiceV2ModifyInvoice
from swagger_client.models.all_oftns_modify_invoice_v2_result_modify_invoice import AllOftnsModifyInvoiceV2ResultModifyInvoice
from swagger_client.models.all_oftns_modify_invoice_v3_modify_invoice import AllOftnsModifyInvoiceV3ModifyInvoice
from swagger_client.models.all_oftns_modify_invoice_v3_result_modify_invoice import AllOftnsModifyInvoiceV3ResultModifyInvoice
from swagger_client.models.all_oftns_modify_invoice_v4_modify_invoice import AllOftnsModifyInvoiceV4ModifyInvoice
from swagger_client.models.all_oftns_modify_invoice_v4_result_modify_invoice import AllOftnsModifyInvoiceV4ResultModifyInvoice
from swagger_client.models.change_contact_information import ChangeContactInformation
from swagger_client.models.change_contact_information_body import ChangeContactInformationBody
from swagger_client.models.change_contact_information_result import ChangeContactInformationResult
from swagger_client.models.change_customer_address import ChangeCustomerAddress
from swagger_client.models.change_customer_address_body import ChangeCustomerAddressBody
from swagger_client.models.change_customer_address_result import ChangeCustomerAddressResult
from swagger_client.models.change_customer_address_v2 import ChangeCustomerAddressV2
from swagger_client.models.change_customer_address_v2_body import ChangeCustomerAddressV2Body
from swagger_client.models.change_customer_address_v2_result import ChangeCustomerAddressV2Result
from swagger_client.models.change_invoice_address import ChangeInvoiceAddress
from swagger_client.models.change_invoice_address_body import ChangeInvoiceAddressBody
from swagger_client.models.change_invoice_address_result import ChangeInvoiceAddressResult
from swagger_client.models.confirm_invoice import ConfirmInvoice
from swagger_client.models.confirm_invoice_body import ConfirmInvoiceBody
from swagger_client.models.confirm_invoice_result import ConfirmInvoiceResult
from swagger_client.models.inline_response200 import InlineResponse200
from swagger_client.models.inline_response2001 import InlineResponse2001
from swagger_client.models.inline_response20010 import InlineResponse20010
from swagger_client.models.inline_response20011 import InlineResponse20011
from swagger_client.models.inline_response20012 import InlineResponse20012
from swagger_client.models.inline_response20013 import InlineResponse20013
from swagger_client.models.inline_response2002 import InlineResponse2002
from swagger_client.models.inline_response2003 import InlineResponse2003
from swagger_client.models.inline_response2004 import InlineResponse2004
from swagger_client.models.inline_response2005 import InlineResponse2005
from swagger_client.models.inline_response2006 import InlineResponse2006
from swagger_client.models.inline_response2007 import InlineResponse2007
from swagger_client.models.inline_response2008 import InlineResponse2008
from swagger_client.models.inline_response2009 import InlineResponse2009
from swagger_client.models.insert_payment import InsertPayment
from swagger_client.models.insert_payment_body import InsertPaymentBody
from swagger_client.models.insert_payment_result import InsertPaymentResult
from swagger_client.models.insert_payment_v2 import InsertPaymentV2
from swagger_client.models.insert_payment_v2_body import InsertPaymentV2Body
from swagger_client.models.insert_payment_v2_result import InsertPaymentV2Result
from swagger_client.models.insert_payment_v3 import InsertPaymentV3
from swagger_client.models.insert_payment_v3_body import InsertPaymentV3Body
from swagger_client.models.insert_payment_v3_result import InsertPaymentV3Result
from swagger_client.models.modify_hotel_bank_account_info import ModifyHotelBankAccountInfo
from swagger_client.models.modify_hotel_bank_account_info_body import ModifyHotelBankAccountInfoBody
from swagger_client.models.modify_hotel_bank_account_info_result import ModifyHotelBankAccountInfoResult
from swagger_client.models.modify_hotel_credit_card_info import ModifyHotelCreditCardInfo
from swagger_client.models.modify_hotel_credit_card_info_body import ModifyHotelCreditCardInfoBody
from swagger_client.models.modify_hotel_credit_card_info_result import ModifyHotelCreditCardInfoResult
from swagger_client.models.modify_invoice import ModifyInvoice
from swagger_client.models.modify_invoice_body import ModifyInvoiceBody
from swagger_client.models.modify_invoice_result import ModifyInvoiceResult
from swagger_client.models.modify_invoice_v2 import ModifyInvoiceV2
from swagger_client.models.modify_invoice_v2_body import ModifyInvoiceV2Body
from swagger_client.models.modify_invoice_v2_result import ModifyInvoiceV2Result
from swagger_client.models.modify_invoice_v3 import ModifyInvoiceV3
from swagger_client.models.modify_invoice_v3_body import ModifyInvoiceV3Body
from swagger_client.models.modify_invoice_v3_result import ModifyInvoiceV3Result
from swagger_client.models.modify_invoice_v4 import ModifyInvoiceV4
from swagger_client.models.modify_invoice_v4_body import ModifyInvoiceV4Body
from swagger_client.models.modify_invoice_v4_result import ModifyInvoiceV4Result
from swagger_client.models.q10_invoice import Q10Invoice
from swagger_client.models.q10_invoice_address import Q10InvoiceAddress
from swagger_client.models.q10_invoice_list import Q10InvoiceList
from swagger_client.models.q10_positions import Q10Positions
from swagger_client.models.q12_document import Q12Document
from swagger_client.models.q12_documents import Q12Documents
from swagger_client.models.q12_payment_line import Q12PaymentLine
from swagger_client.models.q12_payment_lines import Q12PaymentLines
from swagger_client.models.q14_customer import Q14Customer
from swagger_client.models.q14_customer_list import Q14CustomerList
from swagger_client.models.q16_invoice import Q16Invoice
from swagger_client.models.q16_invoice_address import Q16InvoiceAddress
from swagger_client.models.q16_invoice_list import Q16InvoiceList
from swagger_client.models.q16_positions import Q16Positions
from swagger_client.models.q18_invoice import Q18Invoice
from swagger_client.models.q18_invoice_address import Q18InvoiceAddress
from swagger_client.models.q18_invoice_list import Q18InvoiceList
from swagger_client.models.q18_positions import Q18Positions
from swagger_client.models.q20_document import Q20Document
from swagger_client.models.q20_documents import Q20Documents
from swagger_client.models.q20_payment_line import Q20PaymentLine
from swagger_client.models.q20_payment_lines import Q20PaymentLines
from swagger_client.models.q22_invoice import Q22Invoice
from swagger_client.models.q22_invoice_address import Q22InvoiceAddress
from swagger_client.models.q22_invoice_list import Q22InvoiceList
from swagger_client.models.q22_positions import Q22Positions
from swagger_client.models.q24_invoice import Q24Invoice
from swagger_client.models.q24_invoice_list import Q24InvoiceList
from swagger_client.models.q26_hotel_credit_card_info import Q26HotelCreditCardInfo
from swagger_client.models.q26_hotel_credit_card_info_list import Q26HotelCreditCardInfoList
from swagger_client.models.q28_hotel_bank_account_info import Q28HotelBankAccountInfo
from swagger_client.models.q28_hotel_bank_account_info_list import Q28HotelBankAccountInfoList
from swagger_client.models.q2_invoice import Q2Invoice
from swagger_client.models.q2_invoices import Q2Invoices
from swagger_client.models.q4_customer import Q4Customer
from swagger_client.models.q4_customer_list import Q4CustomerList
from swagger_client.models.q6_contact import Q6Contact
from swagger_client.models.q6_contact_list import Q6ContactList
from swagger_client.models.q8_document import Q8Document
from swagger_client.models.q8_documents import Q8Documents
from swagger_client.models.q8_payment_line import Q8PaymentLine
from swagger_client.models.q8_payment_lines import Q8PaymentLines
from swagger_client.models.tns_change_contact_information import TnsChangeContactInformation
from swagger_client.models.tns_change_contact_information_result import TnsChangeContactInformationResult
from swagger_client.models.tns_change_customer_address import TnsChangeCustomerAddress
from swagger_client.models.tns_change_customer_address_result import TnsChangeCustomerAddressResult
from swagger_client.models.tns_change_customer_address_v2 import TnsChangeCustomerAddressV2
from swagger_client.models.tns_change_customer_address_v2_result import TnsChangeCustomerAddressV2Result
from swagger_client.models.tns_change_invoice_address import TnsChangeInvoiceAddress
from swagger_client.models.tns_change_invoice_address_result import TnsChangeInvoiceAddressResult
from swagger_client.models.tns_confirm_invoice import TnsConfirmInvoice
from swagger_client.models.tns_confirm_invoice_result import TnsConfirmInvoiceResult
from swagger_client.models.tns_insert_payment import TnsInsertPayment
from swagger_client.models.tns_insert_payment_result import TnsInsertPaymentResult
from swagger_client.models.tns_insert_payment_v2 import TnsInsertPaymentV2
from swagger_client.models.tns_insert_payment_v2_result import TnsInsertPaymentV2Result
from swagger_client.models.tns_insert_payment_v3 import TnsInsertPaymentV3
from swagger_client.models.tns_insert_payment_v3_result import TnsInsertPaymentV3Result
from swagger_client.models.tns_modify_hotel_bank_account_info import TnsModifyHotelBankAccountInfo
from swagger_client.models.tns_modify_hotel_bank_account_info_result import TnsModifyHotelBankAccountInfoResult
from swagger_client.models.tns_modify_hotel_credit_card_info import TnsModifyHotelCreditCardInfo
from swagger_client.models.tns_modify_hotel_credit_card_info_result import TnsModifyHotelCreditCardInfoResult
from swagger_client.models.tns_modify_invoice import TnsModifyInvoice
from swagger_client.models.tns_modify_invoice_result import TnsModifyInvoiceResult
from swagger_client.models.tns_modify_invoice_v2 import TnsModifyInvoiceV2
from swagger_client.models.tns_modify_invoice_v2_result import TnsModifyInvoiceV2Result
from swagger_client.models.tns_modify_invoice_v3 import TnsModifyInvoiceV3
from swagger_client.models.tns_modify_invoice_v3_result import TnsModifyInvoiceV3Result
from swagger_client.models.tns_modify_invoice_v4 import TnsModifyInvoiceV4
from swagger_client.models.tns_modify_invoice_v4_result import TnsModifyInvoiceV4Result
