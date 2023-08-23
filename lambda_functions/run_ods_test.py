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
        print("<<testChangeInvoiceAddress response received!")
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
        print("<<testChangeCustomerAddressV2 response received!")
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
        print("<<testConfirmInvoice response received!")
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
        print("<<testChangeContactInformation response received!")
    except Exception as e:
        print(str(e))
        return False

    return True

def testInsertPaymentV3():

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

    body = ods_client.InsertPaymentV3(tnsinsertpaymentv3)

    try:
        api_response = api_instance.insert_payment_v3(body)
        print("<<testInsertPaymentV3 response received!")
    except Exception as e:
        print(str(e))
        return False

    return True

def testInsertPaymentPC():
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
        print("<<testInsertPaymentPC response received!")
    except Exception as e:
        print(str(e))
        return False

    return True


def testModifyInvoiceV4():
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
    body = ods_client.ModifyInvoiceV4(tns_modifyinvoicev4) 

    try:
        # ModifyInvoiceV4
        api_response = api_instance.modify_invoice_v4(body)
        print("<<testModifyInvoiceV4 response received!")
    except Exception as e:
        print(str(e))
        return False

    return True

def testModifyHotelCreditCardInfo():
    api_instance = ods_client.HPPBindingApi()

    q26_hotelcreditcardinfo = ods_client.Q26HotelCreditCardInfo(
        customer_no = "customer_no",
        pcn = 0,
        expiry = "expiry",
        company = "company",
        authorization_date = "authorization_date",
        state = ["state"],
        scheme_reference_id = "scheme_reference_id"
    )

    hotelcreditcardinfo_list = []
    hotelcreditcardinfo_list.append(q26_hotelcreditcardinfo)

    q26_hotelcreditcardinfolist = ods_client.Q26HotelCreditCardInfoList(hotelcreditcardinfo_list)
    tns_modifyhotelcreditcardinfo = ods_client.TnsModifyHotelCreditCardInfo(q26_hotelcreditcardinfolist)
    body = ods_client.ModifyHotelCreditCardInfo(tns_modifyhotelcreditcardinfo)

    try:
        api_response = api_instance.modify_hotel_credit_card_info(body)
        print("<<testModifyHotelCreditCardInfo response received!")
    except Exception as e:
        print(str(e))
        return False

    return True

def testModifyHotelBankAccountInfo():

    api_instance = ods_client.HPPBindingApi()

    Q28HotelBankAccountInfo = ods_client.Q28HotelBankAccountInfo(
        customer_no = "customer_no",
        state = "state",
        iban = "iban",
        bic = "bic",
        account_owner = "account_owner",
        mandate_id = "mandate_id"
    )

    Q28HotelBankAccountInfoList = ods_client.Q28HotelBankAccountInfoList([Q28HotelBankAccountInfo])

    TnsModifyHotelBankAccountInfo = ods_client.TnsModifyHotelBankAccountInfo(Q28HotelBankAccountInfoList)

    body = ods_client.ModifyHotelBankAccountInfo(TnsModifyHotelBankAccountInfo)

    try:
        api_response = api_instance.modify_hotel_bank_account_info(body)
        print("<<testModifyHotelBankAccountInfo response received!")
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

    if not testChangeContactInformation():
        return {
            'statusCode': 500,
            'api': 'change_contact_information'
        }

    if not testInsertPaymentV3():
        return {
            'statusCode': 500,
            'api': 'insert_payment_v3'
        }

    if not testInsertPaymentPC():
        return {
            'statusCode': 500,
            'api': 'insert_payment_pc'
        }

    if not testModifyInvoiceV4():
        return {
            'statusCode': 500,
            'api': 'modify_invoice_v4'
        }

    if not testModifyHotelCreditCardInfo():
        return {
            'statusCode': 500,
            'api': 'modify_hotel_credit_card_info'
        }

    if not testModifyHotelBankAccountInfo():
        return {
            'statusCode': 500,
            'api': 'modify_hotel_bank_account_info'
        }

    return {
        'statusCode': 200,
        'error': 'OK'
    }

if __name__ == '__main__':
    run(None, None)
