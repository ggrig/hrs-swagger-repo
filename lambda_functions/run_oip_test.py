import json
import oip_client

def test(api_instance): return True

def testAccountingDocument(api_instance):

    position = oip_client.Position(
        company = "HRS",
        process_number = 162621580,
        reservation_no = 283301172,
        position_no = 1,
        client_guestname1 = "CANSECO AQUINO, ALEJANDRO CLAUDIO",
        client_guestname2 = "string",
        client_company = "VW Cytric_Mexiko",
        room_type = 0,
        number_of_rooms = 1,
        number_of_person = 0,
        breakfast_approval_status = "0",
        arrival_date = "2023-08-15",
        departure_date = "2023-08-15",
        number_of_nights = 2,
        rate_description = "VolkswagenAG",
        rate_type = 21011,
        breakfast_type = 0,
        breakfast_price = 0,
        currency_factor = 18.90034,
        currency_code = "MXN",
        commission_amount = 1500,
        comission_rate = 0,
        room_price = 1500,
        ranking_booster = 0,
        booking_quality = 0,
        booking_code = "string",
        quality_at = "2023-08-15T06:59:55.198Z",
        quality_by_user = "string",
        reservation_source = "81",
        deduction_type = 0,
        calculated_with_function_id = "CalculatedWithFunctionID",
        customer_no = "378128",
        taf_line_amount = 94.5,
        agency_line_amount = 0,
        line_amount = 94.5,
        line_amount_including_vat = 94.5,
        amount_including_vat = 1500,
        total_amount_including_vat = 3000
    )

    body = oip_client.AccountingDocument(
        amount_currency_code = 'MXN',
        company = "string",
        confirmed = False,
        correction_from_document_no = "string",
        customer_no = 378128,
        debitor_currency_rate = 18.90034,
        description = "Rechnung R010876989",
        document_date = "2023-08-15" ,
        document_no = "16846361",
        document_type = "Payment",
        exchange_rate = 1,
        external_document_no = "string",
        fapiao_no = "string" ,
        foreign_currency_code = "MXN",
        has_pdf = False,
        hotel_address_city = "Col. El Coecillo,Leon",
        hotel_address_country_region_code = "102",
        hotel_address_line1 = "Bulevar Adolfo Lopez Mateos 2611",
        hotel_address_line2 = "string" ,
        hotel_address_name = "Radisson Poliforum Plaza Hotel Leon",
        hotel_address_name2 = "string",
        hotel_address_post_code = "37260",
        invoice_address_city = "Col. El Coecillo,Leon",
        invoice_address_contact_no = "string",
        invoice_address_country_region_code = "102",
        invoice_address_customer_no = "378128",
        invoice_address_email = "string",
        invoice_address_line1 = "Bulevar Adolfo Lopez Mateos 2611",
        invoice_address_line2 = "string",
        invoice_address_name = "Radisson Poliforum Plaza Hotel Leon",
        invoice_address_name2 = "string",
        invoice_address_post_code = "37260",
        invoice_exchange_rate = 18.90034,
        ledger_entry_no = 0,
        local_currency_code = "EUR",
        open = True,
        orig_number_of_nights = 4,
        original_amount_gross = 189,
        original_amount_net = 189,
        original_amount_vat = 0,
        original_foreign_amount_gross = 189,
        original_local_amount_gross = 10,
        posting_date = "2023-08-15",
        remaining_amount_gross = 189,
        remaining_amount_net = 189,
        remaining_amount_vat = 0,
        remaining_foreign_amount_gross = 189,
        remaining_local_amount_gross = 10,
        salesperson_code = "FREESALE",
        positions = [position]
    ) # AccountingDocument | 

    document_id = 'document_id'
    try:
        # InsertPayment
        api_response = api_instance.accountingdocuments_document_id_put(body, document_id)
        print("<<testAccountingDocument response received")
    except Exception as e:
        print (str(e))
        return False

    return True

def testBankaccountinfoBody(api_instance):
    body = oip_client.BankaccountinfoBody() # BankaccountinfoBody | 

    try:
        # Create Bank Accout Source
        api_response = api_instance.bank_account_info_post(body)
        print("<<testBankaccountinfoBody response received")
    except Exception as e:
        print (str(e))
        return False

    return True

def testBookingsourceBody(api_instance):
    body = oip_client.BookingsourceBody() # BookingsourceBody | 

    try:
        # Create Booking Source
        api_response = api_instance.booking_source_post(body)
        print("<<testBookingsourceBody response received")
    except Exception as e:
        print (str(e))
        return False

    return True

def testCountriesBody(api_instance):
    body = oip_client.CountriesBody() # CountriesBody | 

    try:
        # Create Countries Source
        api_response = api_instance.countries_post(body)
        print("<<testCountriesBody response received")
    except Exception as e:
        print (str(e))
        return False

    return True

def testHotelsBody(api_instance):
    body = oip_client.HotelsBody() # HotelsBody | 

    try:
        # Create Hotels Source
        api_response = api_instance.hotels_post(body)
        print("<<testHotelsBody response received")
    except Exception as e:
        print (str(e))
        return False

    return True

def testPaymentmethodsBody(api_instance):
    body = oip_client.PaymentmethodsBody() # PaymentmethodsBody | 

    try:
        # Create Payment Methods Source
        api_response = api_instance.payment_methods_post(body)
        print("<<testPaymentmethodsBody response received")
    except Exception as e:
        print (str(e))
        return False

    return True

def testSalespersonBody(api_instance):
    body = oip_client.SalespersonBody() # SalespersonBody |

    try:
        # Create Salesperson Source
        api_response = api_instance.salesperson_post(body)
        print("<<testSalespersonBody response received")
    except Exception as e:
        print (str(e))
        return False

    return True

def run(event, context):

    configuration = oip_client.Configuration()
    api_instance = oip_client.DefaultApi(oip_client.ApiClient(configuration))

    if not testAccountingDocument(api_instance):
        return {
            'statusCode': 500,
            'api': 'accountingdocuments_document_id_put'
        }

    if not test(api_instance):
        return {
            'statusCode': 500,
            'api': 'bank_account_info_post'
        }

    if not test(api_instance):
        return {
            'statusCode': 500,
            'api': 'booking_source_post'
        }

    if not test(api_instance):
        return {
            'statusCode': 500,
            'api': 'countries_post'
        }

    if not test(api_instance):
        return {
            'statusCode': 500,
            'api': 'hotels_post'
        }

    if not test(api_instance):
        return {
            'statusCode': 500,
            'api': 'payment_methods_post'
        }

    if not test(api_instance):
        return {
            'statusCode': 500,
            'api': 'salesperson_post'
        }

    return {
        'statusCode': 200,
        'error': 'OK'
    }

if __name__ == '__main__':
    run(None, None)
