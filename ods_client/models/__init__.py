# coding: utf-8

# flake8: noqa
"""
    HPP-V2

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

# import models into model package
from ods_client.models.all_of_change_contact_information_change_contact_information import AllOfChangeContactInformationChangeContactInformation
from ods_client.models.all_of_change_contact_information_result_change_contact_information_result import AllOfChangeContactInformationResultChangeContactInformationResult
from ods_client.models.all_of_change_customer_address_change_customer_address import AllOfChangeCustomerAddressChangeCustomerAddress
from ods_client.models.all_of_change_customer_address_result_change_customer_address_result import AllOfChangeCustomerAddressResultChangeCustomerAddressResult
from ods_client.models.all_of_change_customer_address_v2_change_customer_address_v2 import AllOfChangeCustomerAddressV2ChangeCustomerAddressV2
from ods_client.models.all_of_change_customer_address_v2_result_change_customer_address_v2_result import AllOfChangeCustomerAddressV2ResultChangeCustomerAddressV2Result
from ods_client.models.all_of_change_invoice_address_change_invoice_address import AllOfChangeInvoiceAddressChangeInvoiceAddress
from ods_client.models.all_of_change_invoice_address_result_change_invoice_address_result import AllOfChangeInvoiceAddressResultChangeInvoiceAddressResult
from ods_client.models.all_of_confirm_invoice_confirm_invoice import AllOfConfirmInvoiceConfirmInvoice
from ods_client.models.all_of_confirm_invoice_result_confirm_invoice_result import AllOfConfirmInvoiceResultConfirmInvoiceResult
from ods_client.models.all_of_insert_payment_insert_payment import AllOfInsertPaymentInsertPayment
from ods_client.models.all_of_insert_payment_pc_insert_payment_pc import AllOfInsertPaymentPCInsertPaymentPc
from ods_client.models.all_of_insert_payment_pc_result_insert_payment_pc_result import AllOfInsertPaymentPCResultInsertPaymentPcResult
from ods_client.models.all_of_insert_payment_result_insert_payment_result import AllOfInsertPaymentResultInsertPaymentResult
from ods_client.models.all_of_insert_payment_v2_insert_payment_v2 import AllOfInsertPaymentV2InsertPaymentV2
from ods_client.models.all_of_insert_payment_v2_result_insert_payment_v2_result import AllOfInsertPaymentV2ResultInsertPaymentV2Result
from ods_client.models.all_of_insert_payment_v3_insert_payment_v3 import AllOfInsertPaymentV3InsertPaymentV3
from ods_client.models.all_of_insert_payment_v3_result_insert_payment_v3_result import AllOfInsertPaymentV3ResultInsertPaymentV3Result
from ods_client.models.all_of_modify_hotel_bank_account_info_modify_hotel_bank_account_info import AllOfModifyHotelBankAccountInfoModifyHotelBankAccountInfo
from ods_client.models.all_of_modify_hotel_bank_account_info_result_modify_hotel_bank_account_info_result import AllOfModifyHotelBankAccountInfoResultModifyHotelBankAccountInfoResult
from ods_client.models.all_of_modify_hotel_credit_card_info_modify_hotel_credit_card_info import AllOfModifyHotelCreditCardInfoModifyHotelCreditCardInfo
from ods_client.models.all_of_modify_hotel_credit_card_info_result_modify_hotel_credit_card_info_result import AllOfModifyHotelCreditCardInfoResultModifyHotelCreditCardInfoResult
from ods_client.models.all_of_modify_invoice_modify_invoice import AllOfModifyInvoiceModifyInvoice
from ods_client.models.all_of_modify_invoice_result_modify_invoice_result import AllOfModifyInvoiceResultModifyInvoiceResult
from ods_client.models.all_of_modify_invoice_v2_modify_invoice_v2 import AllOfModifyInvoiceV2ModifyInvoiceV2
from ods_client.models.all_of_modify_invoice_v2_result_modify_invoice_v2_result import AllOfModifyInvoiceV2ResultModifyInvoiceV2Result
from ods_client.models.all_of_modify_invoice_v3_modify_invoice_v3 import AllOfModifyInvoiceV3ModifyInvoiceV3
from ods_client.models.all_of_modify_invoice_v3_result_modify_invoice_v3_result import AllOfModifyInvoiceV3ResultModifyInvoiceV3Result
from ods_client.models.all_of_modify_invoice_v4_modify_invoice_v4 import AllOfModifyInvoiceV4ModifyInvoiceV4
from ods_client.models.all_of_modify_invoice_v4_result_modify_invoice_v4_result import AllOfModifyInvoiceV4ResultModifyInvoiceV4Result
from ods_client.models.all_ofq10_invoice_invoice_address import AllOfq10InvoiceInvoiceAddress
from ods_client.models.all_ofq12_payment_line_documents import AllOfq12PaymentLineDocuments
from ods_client.models.all_ofq16_invoice_invoice_address import AllOfq16InvoiceInvoiceAddress
from ods_client.models.all_ofq18_invoice_invoice_address import AllOfq18InvoiceInvoiceAddress
from ods_client.models.all_ofq20_payment_line_documents import AllOfq20PaymentLineDocuments
from ods_client.models.all_ofq22_invoice_invoice_address import AllOfq22InvoiceInvoiceAddress
from ods_client.models.all_ofq30_payment_line_reservation import AllOfq30PaymentLineReservation
from ods_client.models.all_ofq8_payment_line_documents import AllOfq8PaymentLineDocuments
from ods_client.models.all_oftns_change_contact_information_contact_information import AllOftnsChangeContactInformationContactInformation
from ods_client.models.all_oftns_change_contact_information_result_contact_information import AllOftnsChangeContactInformationResultContactInformation
from ods_client.models.all_oftns_change_customer_address_customer_address import AllOftnsChangeCustomerAddressCustomerAddress
from ods_client.models.all_oftns_change_customer_address_result_customer_address import AllOftnsChangeCustomerAddressResultCustomerAddress
from ods_client.models.all_oftns_change_customer_address_v2_customer_address import AllOftnsChangeCustomerAddressV2CustomerAddress
from ods_client.models.all_oftns_change_customer_address_v2_result_customer_address import AllOftnsChangeCustomerAddressV2ResultCustomerAddress
from ods_client.models.all_oftns_change_invoice_address_invoice_address import AllOftnsChangeInvoiceAddressInvoiceAddress
from ods_client.models.all_oftns_change_invoice_address_result_invoice_address import AllOftnsChangeInvoiceAddressResultInvoiceAddress
from ods_client.models.all_oftns_confirm_invoice_confirm_invoice import AllOftnsConfirmInvoiceConfirmInvoice
from ods_client.models.all_oftns_confirm_invoice_result_confirm_invoice import AllOftnsConfirmInvoiceResultConfirmInvoice
from ods_client.models.all_oftns_insert_payment_insert_payment import AllOftnsInsertPaymentInsertPayment
from ods_client.models.all_oftns_insert_payment_pc_insert_payment import AllOftnsInsertPaymentPCInsertPayment
from ods_client.models.all_oftns_insert_payment_pc_result_insert_payment import AllOftnsInsertPaymentPCResultInsertPayment
from ods_client.models.all_oftns_insert_payment_result_insert_payment import AllOftnsInsertPaymentResultInsertPayment
from ods_client.models.all_oftns_insert_payment_v2_insert_payment import AllOftnsInsertPaymentV2InsertPayment
from ods_client.models.all_oftns_insert_payment_v2_result_insert_payment import AllOftnsInsertPaymentV2ResultInsertPayment
from ods_client.models.all_oftns_insert_payment_v3_insert_payment import AllOftnsInsertPaymentV3InsertPayment
from ods_client.models.all_oftns_insert_payment_v3_result_insert_payment import AllOftnsInsertPaymentV3ResultInsertPayment
from ods_client.models.all_oftns_modify_hotel_bank_account_info_modify_bank_acc_info import AllOftnsModifyHotelBankAccountInfoModifyBankAccInfo
from ods_client.models.all_oftns_modify_hotel_bank_account_info_result_modify_bank_acc_info import AllOftnsModifyHotelBankAccountInfoResultModifyBankAccInfo
from ods_client.models.all_oftns_modify_hotel_credit_card_info_modify_credit_card_info import AllOftnsModifyHotelCreditCardInfoModifyCreditCardInfo
from ods_client.models.all_oftns_modify_hotel_credit_card_info_result_modify_credit_card_info import AllOftnsModifyHotelCreditCardInfoResultModifyCreditCardInfo
from ods_client.models.all_oftns_modify_invoice_modify_invoice import AllOftnsModifyInvoiceModifyInvoice
from ods_client.models.all_oftns_modify_invoice_result_modify_invoice import AllOftnsModifyInvoiceResultModifyInvoice
from ods_client.models.all_oftns_modify_invoice_v2_modify_invoice import AllOftnsModifyInvoiceV2ModifyInvoice
from ods_client.models.all_oftns_modify_invoice_v2_result_modify_invoice import AllOftnsModifyInvoiceV2ResultModifyInvoice
from ods_client.models.all_oftns_modify_invoice_v3_modify_invoice import AllOftnsModifyInvoiceV3ModifyInvoice
from ods_client.models.all_oftns_modify_invoice_v3_result_modify_invoice import AllOftnsModifyInvoiceV3ResultModifyInvoice
from ods_client.models.all_oftns_modify_invoice_v4_modify_invoice import AllOftnsModifyInvoiceV4ModifyInvoice
from ods_client.models.all_oftns_modify_invoice_v4_result_modify_invoice import AllOftnsModifyInvoiceV4ResultModifyInvoice
from ods_client.models.change_contact_information import ChangeContactInformation
from ods_client.models.change_contact_information_body import ChangeContactInformationBody
from ods_client.models.change_contact_information_result import ChangeContactInformationResult
from ods_client.models.change_customer_address import ChangeCustomerAddress
from ods_client.models.change_customer_address_body import ChangeCustomerAddressBody
from ods_client.models.change_customer_address_result import ChangeCustomerAddressResult
from ods_client.models.change_customer_address_v2 import ChangeCustomerAddressV2
from ods_client.models.change_customer_address_v2_body import ChangeCustomerAddressV2Body
from ods_client.models.change_customer_address_v2_result import ChangeCustomerAddressV2Result
from ods_client.models.change_invoice_address import ChangeInvoiceAddress
from ods_client.models.change_invoice_address_body import ChangeInvoiceAddressBody
from ods_client.models.change_invoice_address_result import ChangeInvoiceAddressResult
from ods_client.models.confirm_invoice import ConfirmInvoice
from ods_client.models.confirm_invoice_body import ConfirmInvoiceBody
from ods_client.models.confirm_invoice_result import ConfirmInvoiceResult
from ods_client.models.inline_response200 import InlineResponse200
from ods_client.models.inline_response2001 import InlineResponse2001
from ods_client.models.inline_response20010 import InlineResponse20010
from ods_client.models.inline_response20011 import InlineResponse20011
from ods_client.models.inline_response20012 import InlineResponse20012
from ods_client.models.inline_response20013 import InlineResponse20013
from ods_client.models.inline_response20014 import InlineResponse20014
from ods_client.models.inline_response2002 import InlineResponse2002
from ods_client.models.inline_response2003 import InlineResponse2003
from ods_client.models.inline_response2004 import InlineResponse2004
from ods_client.models.inline_response2005 import InlineResponse2005
from ods_client.models.inline_response2006 import InlineResponse2006
from ods_client.models.inline_response2007 import InlineResponse2007
from ods_client.models.inline_response2008 import InlineResponse2008
from ods_client.models.inline_response2009 import InlineResponse2009
from ods_client.models.insert_payment import InsertPayment
from ods_client.models.insert_payment_body import InsertPaymentBody
from ods_client.models.insert_payment_pc import InsertPaymentPC
from ods_client.models.insert_payment_pc_body import InsertPaymentPCBody
from ods_client.models.insert_payment_pc_result import InsertPaymentPCResult
from ods_client.models.insert_payment_result import InsertPaymentResult
from ods_client.models.insert_payment_v2 import InsertPaymentV2
from ods_client.models.insert_payment_v2_body import InsertPaymentV2Body
from ods_client.models.insert_payment_v2_result import InsertPaymentV2Result
from ods_client.models.insert_payment_v3 import InsertPaymentV3
from ods_client.models.insert_payment_v3_body import InsertPaymentV3Body
from ods_client.models.insert_payment_v3_result import InsertPaymentV3Result
from ods_client.models.modify_hotel_bank_account_info import ModifyHotelBankAccountInfo
from ods_client.models.modify_hotel_bank_account_info_body import ModifyHotelBankAccountInfoBody
from ods_client.models.modify_hotel_bank_account_info_result import ModifyHotelBankAccountInfoResult
from ods_client.models.modify_hotel_credit_card_info import ModifyHotelCreditCardInfo
from ods_client.models.modify_hotel_credit_card_info_body import ModifyHotelCreditCardInfoBody
from ods_client.models.modify_hotel_credit_card_info_result import ModifyHotelCreditCardInfoResult
from ods_client.models.modify_invoice import ModifyInvoice
from ods_client.models.modify_invoice_body import ModifyInvoiceBody
from ods_client.models.modify_invoice_result import ModifyInvoiceResult
from ods_client.models.modify_invoice_v2 import ModifyInvoiceV2
from ods_client.models.modify_invoice_v2_body import ModifyInvoiceV2Body
from ods_client.models.modify_invoice_v2_result import ModifyInvoiceV2Result
from ods_client.models.modify_invoice_v3 import ModifyInvoiceV3
from ods_client.models.modify_invoice_v3_body import ModifyInvoiceV3Body
from ods_client.models.modify_invoice_v3_result import ModifyInvoiceV3Result
from ods_client.models.modify_invoice_v4 import ModifyInvoiceV4
from ods_client.models.modify_invoice_v4_body import ModifyInvoiceV4Body
from ods_client.models.modify_invoice_v4_result import ModifyInvoiceV4Result
from ods_client.models.q10_invoice import Q10Invoice
from ods_client.models.q10_invoice_address import Q10InvoiceAddress
from ods_client.models.q10_invoice_list import Q10InvoiceList
from ods_client.models.q10_positions import Q10Positions
from ods_client.models.q12_document import Q12Document
from ods_client.models.q12_documents import Q12Documents
from ods_client.models.q12_payment_line import Q12PaymentLine
from ods_client.models.q12_payment_lines import Q12PaymentLines
from ods_client.models.q14_customer import Q14Customer
from ods_client.models.q14_customer_list import Q14CustomerList
from ods_client.models.q16_invoice import Q16Invoice
from ods_client.models.q16_invoice_address import Q16InvoiceAddress
from ods_client.models.q16_invoice_list import Q16InvoiceList
from ods_client.models.q16_positions import Q16Positions
from ods_client.models.q18_invoice import Q18Invoice
from ods_client.models.q18_invoice_address import Q18InvoiceAddress
from ods_client.models.q18_invoice_list import Q18InvoiceList
from ods_client.models.q18_positions import Q18Positions
from ods_client.models.q20_document import Q20Document
from ods_client.models.q20_documents import Q20Documents
from ods_client.models.q20_payment_line import Q20PaymentLine
from ods_client.models.q20_payment_lines import Q20PaymentLines
from ods_client.models.q22_invoice import Q22Invoice
from ods_client.models.q22_invoice_address import Q22InvoiceAddress
from ods_client.models.q22_invoice_list import Q22InvoiceList
from ods_client.models.q22_positions import Q22Positions
from ods_client.models.q24_invoice import Q24Invoice
from ods_client.models.q24_invoice_list import Q24InvoiceList
from ods_client.models.q26_hotel_credit_card_info import Q26HotelCreditCardInfo
from ods_client.models.q26_hotel_credit_card_info_list import Q26HotelCreditCardInfoList
from ods_client.models.q28_hotel_bank_account_info import Q28HotelBankAccountInfo
from ods_client.models.q28_hotel_bank_account_info_list import Q28HotelBankAccountInfoList
from ods_client.models.q2_invoice import Q2Invoice
from ods_client.models.q2_invoices import Q2Invoices
from ods_client.models.q30_document import Q30Document
from ods_client.models.q30_payment_line import Q30PaymentLine
from ods_client.models.q30_payment_lines import Q30PaymentLines
from ods_client.models.q30_reservation import Q30Reservation
from ods_client.models.q4_customer import Q4Customer
from ods_client.models.q4_customer_list import Q4CustomerList
from ods_client.models.q6_contact import Q6Contact
from ods_client.models.q6_contact_list import Q6ContactList
from ods_client.models.q8_document import Q8Document
from ods_client.models.q8_documents import Q8Documents
from ods_client.models.q8_payment_line import Q8PaymentLine
from ods_client.models.q8_payment_lines import Q8PaymentLines
from ods_client.models.tns_change_contact_information import TnsChangeContactInformation
from ods_client.models.tns_change_contact_information_result import TnsChangeContactInformationResult
from ods_client.models.tns_change_customer_address import TnsChangeCustomerAddress
from ods_client.models.tns_change_customer_address_result import TnsChangeCustomerAddressResult
from ods_client.models.tns_change_customer_address_v2 import TnsChangeCustomerAddressV2
from ods_client.models.tns_change_customer_address_v2_result import TnsChangeCustomerAddressV2Result
from ods_client.models.tns_change_invoice_address import TnsChangeInvoiceAddress
from ods_client.models.tns_change_invoice_address_result import TnsChangeInvoiceAddressResult
from ods_client.models.tns_confirm_invoice import TnsConfirmInvoice
from ods_client.models.tns_confirm_invoice_result import TnsConfirmInvoiceResult
from ods_client.models.tns_insert_payment import TnsInsertPayment
from ods_client.models.tns_insert_payment_pc import TnsInsertPaymentPC
from ods_client.models.tns_insert_payment_pc_result import TnsInsertPaymentPCResult
from ods_client.models.tns_insert_payment_result import TnsInsertPaymentResult
from ods_client.models.tns_insert_payment_v2 import TnsInsertPaymentV2
from ods_client.models.tns_insert_payment_v2_result import TnsInsertPaymentV2Result
from ods_client.models.tns_insert_payment_v3 import TnsInsertPaymentV3
from ods_client.models.tns_insert_payment_v3_result import TnsInsertPaymentV3Result
from ods_client.models.tns_modify_hotel_bank_account_info import TnsModifyHotelBankAccountInfo
from ods_client.models.tns_modify_hotel_bank_account_info_result import TnsModifyHotelBankAccountInfoResult
from ods_client.models.tns_modify_hotel_credit_card_info import TnsModifyHotelCreditCardInfo
from ods_client.models.tns_modify_hotel_credit_card_info_result import TnsModifyHotelCreditCardInfoResult
from ods_client.models.tns_modify_invoice import TnsModifyInvoice
from ods_client.models.tns_modify_invoice_result import TnsModifyInvoiceResult
from ods_client.models.tns_modify_invoice_v2 import TnsModifyInvoiceV2
from ods_client.models.tns_modify_invoice_v2_result import TnsModifyInvoiceV2Result
from ods_client.models.tns_modify_invoice_v3 import TnsModifyInvoiceV3
from ods_client.models.tns_modify_invoice_v3_result import TnsModifyInvoiceV3Result
from ods_client.models.tns_modify_invoice_v4 import TnsModifyInvoiceV4
from ods_client.models.tns_modify_invoice_v4_result import TnsModifyInvoiceV4Result
