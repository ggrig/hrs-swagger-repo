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

    body = oip_client.BankaccountinfoBody(
        mandate_id = 'LS-000002636',
        auto_pay_enabled = True,
        customer_no = '10021',
        iban = 'DE12270727240018046300',
        swift_code = 'DEUTDEDB276',
        owner = 'Nadxxx Kanyy',
        company = 'HRS'      
    ) # BankaccountinfoBody | 

    try:
        # Create Bank Accout Source
        api_response = api_instance.bank_account_info_post(body)
        print("<<testBankaccountinfoBody response received")
    except Exception as e:
        print (str(e))
        return False

    return True

def testBookingsourceBody(api_instance):
        
    body = oip_client.BookingsourceBody(
        no = 'str',
        category = 'str',
        name = 'str',
        tenant = 'str'            
    ) # BookingsourceBody | 

    try:
        # Create Booking Source
        api_response = api_instance.booking_source_post(body)
        print("<<testBookingsourceBody response received")
    except Exception as e:
        print (str(e))
        return False

    return True

def testCountriesBody(api_instance):

    body = oip_client.CountriesBody(
        name = 'str',
        code = 'str',
        eu_country_region_code = 'str',
        intrastat_code = 'str',
        address_format = 'str',
        contact_address_format = 'str',
        global_dimension2_code = 'str',
        customer_template_code = 'str',
        income_cost_carrier_code = 'str',
        eu_affiliation = 'str',
        continent = 'str',
        max_iban_length = 'str',
        length_of_bank_branch_code = 'str',
        responsibility_center = 'str',
        iso_code = 'str',
        culture_info = 'str',
        signature = 'str',
        primary_language_code = 'str',
        bank_country_code = 'str',
        eu_standard = 'str',
        invoicing_in_local_currency = 'str',
        currency_code = 'str',
        default_length_branch_code = 'str',
        default_length_account_no = 'str',
        iso_bank_code = 'str',
        accounting_period = 'str',
        vat_registration_obligation = 'str',
        vend_gen_bus_posting_group = 'str',
        cust_gen_bus_posting_group = 'str',
        tenant = 'str'            
    ) # CountriesBody | 

    try:
        # Create Countries Source
        api_response = api_instance.countries_post(body)
        print("<<testCountriesBody response received")
    except Exception as e:
        print (str(e))
        return False

    return True

def testHotelsBody(api_instance):

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
        # Create Hotels Source
        api_response = api_instance.hotels_post(body)
        print("<<testHotelsBody response received")
    except Exception as e:
        print (str(e))
        return False

    return True

def testPaymentmethodsBody(api_instance):

    body = oip_client.PaymentmethodsBody(
        code = 'str',
        description = 'str',
        bal_account_type = 'str',
        bal_account_no = 'str',
        surcharge_variable = 'str',
        surcharge_fix = 'str',
        cutoff_amount_variable = 'str',
        fee_account = 'str',
        pay_view_code = 'str',
        cutoff_amount_fee = 'str',
        default_payment_type_code = 'str',
        single_payment = 'str',
        default_pmt_bank_account_no = 'str',
        separate_pmt_proposal_head = 'str',
        vendor_purpose_text = 'str',
        customer_purpose_text = 'str',
        payment_note_purpose_text = 'str',
        vendor_purpose_text_header = 'str',
        purpose_text_footer = 'str',
        limit_payment_amount_lcy = 'str',
        customer_purpose_text_header = 'str',
        limit_lines_per_head = 'str',
        min_pos_payment_note = 'str',
        limit_lines_per_head_x = 'str',
        min_pos_payment_note_x = 'str',
        tenant = 'str'            
    ) # PaymentmethodsBody |

    try:
        # Create Payment Methods Source
        api_response = api_instance.payment_methods_post(body)
        print("<<testPaymentmethodsBody response received")
    except Exception as e:
        print (str(e))
        return False

    return True

def testSalespersonBody(api_instance):

    body = oip_client.SalespersonBody(
        timestamp = 'str',
        code = 'str',
        description = 'str',
        fax_extension = 'str',
        phone_extension = 'str',
        contact_mail = 'str',
        tenant = 'str'            
    ) # SalespersonBody |

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

    if not testBankaccountinfoBody(api_instance):
        return {
            'statusCode': 500,
            'api': 'bank_account_info_post'
        }

    if not testBookingsourceBody(api_instance):
        return {
            'statusCode': 500,
            'api': 'booking_source_post'
        }

    if not testCountriesBody(api_instance):
        return {
            'statusCode': 500,
            'api': 'countries_post'
        }

    if not testHotelsBody(api_instance):
        return {
            'statusCode': 500,
            'api': 'hotels_post'
        }

    if not testPaymentmethodsBody(api_instance):
        return {
            'statusCode': 500,
            'api': 'payment_methods_post'
        }

    if not testSalespersonBody(api_instance):
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
