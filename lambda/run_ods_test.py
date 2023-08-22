import json
import ods_client

def testChangeInvoiceAddress():

    api_instance = ods_client.HPPBindingApi()

    q2_invoice = ods_client.Q2Invoice(
        invoice_no = "string",
        name = "string",
        name2 = "string",
        address = "string",
        address2 = "string",
        city = "string",
        post_code = "string"
    )

    invoice_list = []
    invoice_list.append(q2_invoice)

    q2_invoices = ods_client.Q2Invoices(invoice_list)

    tns_changeinvoiceaddress = ods_client.TnsChangeInvoiceAddress(q2_invoices)
    body = ods_client.ChangeInvoiceAddress(tns_changeinvoiceaddress)

    try:
        api_response = api_instance.change_invoice_address(body)
    except Exception as e:
        print(str(e))
        return False
    
    return True

def testChangeCustomerAddressV2():

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

    body = ods_client.ChangeCustomerAddressV2(tnschangecustomeraddressv2)

    try:
        api_response = api_instance.change_customer_address_v2(body)
    except Exception as e:
        print(str(e))
        return False

    return True

def testConfirmInvoice():

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
        api_response = api_instance.confirm_invoice(body)
    except Exception as e:
        print(str(e))
        return False

    return True

def testChangeContactInformation():

    api_instance = ods_client.HPPBindingApi()

    q6contact = ods_client.Q6Contact(
        contact_no = "contact_no",
        first_name = "first_name",
        middle_name = "middle_name",
        surname = "surname",
        e_mail = "e_mail",
        phone_no = "phone_no",
        fax_no = "fax_no"
    )

    contact_list = []
    contact_list.append(q6contact)

    q6contactlist = ods_client.Q6ContactList(contact_list)

    tnschangecontactinformation = ods_client.TnsChangeContactInformation(q6contactlist)

    body = ods_client.ChangeContactInformation(tnschangecontactinformation)

    try:
        api_response = api_instance.change_contact_information(body)
    except Exception as e:
        print(str(e))
        return False

    return True

def run(event, context):

    if not testChangeInvoiceAddress():
        return {
            'statusCode': 500,
            'api': 'change_invoice_address'
        }

    if not testChangeCustomerAddressV2():
        return {
            'statusCode': 500,
            'api': 'change_customer_address_v2'
        }

    if not testConfirmInvoice():
        return {
            'statusCode': 500,
            'api': 'confirm_invoice'
        }

    if testChangeContactInformation():
        return {
            'statusCode': 500,
            'api': 'change_contact_information'
        }

    # api_instance = ods_client.HPPBindingApi()
    # body = ods_client.InsertPaymentV3() # InsertPaymentV3 | 

    # try:
    #     api_response = api_instance.insert_payment_v3(body)
    # except Exception as e:
    #     return {
    #         'statusCode': 500,
    #         'error': str(e),
    #         'api': 'insert_payment_v3'
    #     }

    # api_instance = ods_client.HPPBindingApi()
    # body = ods_client.InsertPaymentBody() # InsertPaymentBody | 

    # try:
    #     api_response = api_instance.insert_payment(body)
    # except Exception as e:
    #     return {
    #         'statusCode': 500,
    #         'error': str(e),
    #         'api': 'insert_payment'
    #     }

    # api_instance = ods_client.HPPBindingApi()
    # body = ods_client.ModifyInvoiceV4Body() # ModifyInvoiceV4Body | 

    # try:
    #     # ModifyInvoiceV4
    #     api_response = api_instance.modify_invoice_v4(body)
    # except Exception as e:
    #     return {
    #         'statusCode': 500,
    #         'error': str(e),
    #         'api': 'modify_invoice_v4'
    #     }

    # api_instance = ods_client.HPPBindingApi()
    # body = ods_client.ModifyHotelCreditCardInfo() # ModifyHotelCreditCardInfo | 

    # try:
    #     api_response = api_instance.modify_hotel_credit_card_info(body)
    # except Exception as e:
    #     return {
    #         'statusCode': 500,
    #         'error': str(e),
    #         'api': 'modify_hotel_credit_card_info'
    #     }

    # api_instance = ods_client.HPPBindingApi()
    # body = ods_client.ModifyHotelBankAccountInfo() # ModifyHotelBankAccountInfo | 

    # try:
    #     api_response = api_instance.modify_hotel_bank_account_info(body)
    # except Exception as e:
    #     return {
    #         'statusCode': 500,
    #         'error': str(e),
    #         'api': 'modify_hotel_bank_account_info'
    #     }

    return {
        'statusCode': 200,
        'error': 'OK'
    }
