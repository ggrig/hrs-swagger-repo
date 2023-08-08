import json
import ods_client

def run(event, context):

    api_instance = ods_client.HPPBindingApi()
    body = ods_client.ChangeInvoiceAddress() # ChangeInvoiceAddress | 

    try:
        api_response = api_instance.change_invoice_address(body)
    except Exception as e:
        return {
            'statusCode': 500,
            'error': str(e),
            'api': 'change_invoice_address'
        }

    # api_instance = ods_client.HPPBindingApi()
    # body = ods_client.ChangeCustomerAddressV2() # ChangeCustomerAddressV2 | 

    # try:
    #     api_response = api_instance.change_customer_address_v2(body)
    #     pprint(api_response)
    # except Exception as e:
    #     return {
    #         'statusCode': 500,
    #         'error': str(e),
    #         'api': 'change_customer_address_v2'
    #     }

    # api_instance = ods_client.HPPBindingApi()
    # body = ods_client.ConfirmInvoice() # ConfirmInvoice | 

    # try:
    #     api_response = api_instance.confirm_invoice(body)
    #     pprint(api_response)
    # except Exception as e:
    #     return {
    #         'statusCode': 500,
    #         'error': str(e),
    #         'api': 'confirm_invoice'
    #     }

    api_instance = ods_client.HPPBindingApi()
    body = ods_client.ChangeContactInformation() # ChangeContactInformation | 

    try:
        api_response = api_instance.change_contact_information(body)
    except Exception as e:
        return {
            'statusCode': 500,
            'error': str(e),
            'api': 'change_contact_information'
        }

    api_instance = ods_client.HPPBindingApi()
    body = ods_client.InsertPaymentV3() # InsertPaymentV3 | 

    try:
        api_response = api_instance.insert_payment_v3(body)
    except Exception as e:
        return {
            'statusCode': 500,
            'error': str(e),
            'api': 'insert_payment_v3'
        }

    api_instance = ods_client.HPPBindingApi()
    body = ods_client.InsertPaymentBody() # InsertPaymentBody | 

    try:
        api_response = api_instance.insert_payment(body)
    except Exception as e:
        return {
            'statusCode': 500,
            'error': str(e),
            'api': 'insert_payment'
        }

    api_instance = ods_client.HPPBindingApi()
    body = ods_client.ModifyInvoiceV4Body() # ModifyInvoiceV4Body | 

    try:
        # ModifyInvoiceV4
        api_response = api_instance.modify_invoice_v4(body)
    except Exception as e:
        return {
            'statusCode': 500,
            'error': str(e),
            'api': 'modify_invoice_v4'
        }

    api_instance = ods_client.HPPBindingApi()
    body = ods_client.ModifyHotelCreditCardInfo() # ModifyHotelCreditCardInfo | 

    try:
        api_response = api_instance.modify_hotel_credit_card_info(body)
    except Exception as e:
        return {
            'statusCode': 500,
            'error': str(e),
            'api': 'modify_hotel_credit_card_info'
        }

    api_instance = ods_client.HPPBindingApi()
    body = ods_client.ModifyHotelBankAccountInfo() # ModifyHotelBankAccountInfo | 

    try:
        api_response = api_instance.modify_hotel_bank_account_info(body)
    except Exception as e:
        return {
            'statusCode': 500,
            'error': str(e),
            'api': 'modify_hotel_bank_account_info'
        }

    return {
        'statusCode': 200,
        'error': 'OK'
    }
