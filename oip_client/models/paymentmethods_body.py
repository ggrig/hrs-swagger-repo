# coding: utf-8

"""
    OIP API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class PaymentmethodsBody(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'code': 'str',
        'description': 'str',
        'bal_account_type': 'str',
        'bal_account_no': 'str',
        'surcharge_variable': 'str',
        'surcharge_fix': 'str',
        'cutoff_amount_variable': 'str',
        'fee_account': 'str',
        'pay_view_code': 'str',
        'cutoff_amount_fee': 'str',
        'default_payment_type_code': 'str',
        'single_payment': 'str',
        'default_pmt_bank_account_no': 'str',
        'separate_pmt_proposal_head': 'str',
        'vendor_purpose_text': 'str',
        'customer_purpose_text': 'str',
        'payment_note_purpose_text': 'str',
        'vendor_purpose_text_header': 'str',
        'purpose_text_footer': 'str',
        'limit_payment_amount_lcy': 'str',
        'customer_purpose_text_header': 'str',
        'limit_lines_per_head': 'str',
        'min_pos_payment_note': 'str',
        'limit_lines_per_head_x': 'str',
        'min_pos_payment_note_x': 'str',
        'tenant': 'str'
    }

    attribute_map = {
        'code': 'Code',
        'description': 'Description',
        'bal_account_type': 'BalAccountType',
        'bal_account_no': 'BalAccountNo',
        'surcharge_variable': 'SurchargeVariable',
        'surcharge_fix': 'SurchargeFix',
        'cutoff_amount_variable': 'CutoffAmountVariable',
        'fee_account': 'FeeAccount',
        'pay_view_code': 'PayViewCode',
        'cutoff_amount_fee': 'CutoffAmountFee',
        'default_payment_type_code': 'DefaultPaymentTypeCode',
        'single_payment': 'SinglePayment',
        'default_pmt_bank_account_no': 'DefaultPmtBankAccountNo',
        'separate_pmt_proposal_head': 'SeparatePmtProposalHead',
        'vendor_purpose_text': 'VendorPurposeText',
        'customer_purpose_text': 'CustomerPurposeText',
        'payment_note_purpose_text': 'PaymentNotePurposeText',
        'vendor_purpose_text_header': 'VendorPurposeTextHeader',
        'purpose_text_footer': 'PurposeTextFooter',
        'limit_payment_amount_lcy': 'LimitPaymentAmountLCY',
        'customer_purpose_text_header': 'CustomerPurposeTextHeader',
        'limit_lines_per_head': 'LimitLinesPerHead',
        'min_pos_payment_note': 'MinPosPaymentNote',
        'limit_lines_per_head_x': 'LimitLinesPerHeadX',
        'min_pos_payment_note_x': 'MinPosPaymentNoteX',
        'tenant': 'Tenant'
    }

    def __init__(self, code=None, description=None, bal_account_type=None, bal_account_no=None, surcharge_variable=None, surcharge_fix=None, cutoff_amount_variable=None, fee_account=None, pay_view_code=None, cutoff_amount_fee=None, default_payment_type_code=None, single_payment=None, default_pmt_bank_account_no=None, separate_pmt_proposal_head=None, vendor_purpose_text=None, customer_purpose_text=None, payment_note_purpose_text=None, vendor_purpose_text_header=None, purpose_text_footer=None, limit_payment_amount_lcy=None, customer_purpose_text_header=None, limit_lines_per_head=None, min_pos_payment_note=None, limit_lines_per_head_x=None, min_pos_payment_note_x=None, tenant=None):  # noqa: E501
        """PaymentmethodsBody - a model defined in Swagger"""  # noqa: E501
        self._code = None
        self._description = None
        self._bal_account_type = None
        self._bal_account_no = None
        self._surcharge_variable = None
        self._surcharge_fix = None
        self._cutoff_amount_variable = None
        self._fee_account = None
        self._pay_view_code = None
        self._cutoff_amount_fee = None
        self._default_payment_type_code = None
        self._single_payment = None
        self._default_pmt_bank_account_no = None
        self._separate_pmt_proposal_head = None
        self._vendor_purpose_text = None
        self._customer_purpose_text = None
        self._payment_note_purpose_text = None
        self._vendor_purpose_text_header = None
        self._purpose_text_footer = None
        self._limit_payment_amount_lcy = None
        self._customer_purpose_text_header = None
        self._limit_lines_per_head = None
        self._min_pos_payment_note = None
        self._limit_lines_per_head_x = None
        self._min_pos_payment_note_x = None
        self._tenant = None
        self.discriminator = None
        if code is not None:
            self.code = code
        if description is not None:
            self.description = description
        if bal_account_type is not None:
            self.bal_account_type = bal_account_type
        if bal_account_no is not None:
            self.bal_account_no = bal_account_no
        if surcharge_variable is not None:
            self.surcharge_variable = surcharge_variable
        if surcharge_fix is not None:
            self.surcharge_fix = surcharge_fix
        if cutoff_amount_variable is not None:
            self.cutoff_amount_variable = cutoff_amount_variable
        if fee_account is not None:
            self.fee_account = fee_account
        if pay_view_code is not None:
            self.pay_view_code = pay_view_code
        if cutoff_amount_fee is not None:
            self.cutoff_amount_fee = cutoff_amount_fee
        if default_payment_type_code is not None:
            self.default_payment_type_code = default_payment_type_code
        if single_payment is not None:
            self.single_payment = single_payment
        if default_pmt_bank_account_no is not None:
            self.default_pmt_bank_account_no = default_pmt_bank_account_no
        if separate_pmt_proposal_head is not None:
            self.separate_pmt_proposal_head = separate_pmt_proposal_head
        if vendor_purpose_text is not None:
            self.vendor_purpose_text = vendor_purpose_text
        if customer_purpose_text is not None:
            self.customer_purpose_text = customer_purpose_text
        if payment_note_purpose_text is not None:
            self.payment_note_purpose_text = payment_note_purpose_text
        if vendor_purpose_text_header is not None:
            self.vendor_purpose_text_header = vendor_purpose_text_header
        if purpose_text_footer is not None:
            self.purpose_text_footer = purpose_text_footer
        if limit_payment_amount_lcy is not None:
            self.limit_payment_amount_lcy = limit_payment_amount_lcy
        if customer_purpose_text_header is not None:
            self.customer_purpose_text_header = customer_purpose_text_header
        if limit_lines_per_head is not None:
            self.limit_lines_per_head = limit_lines_per_head
        if min_pos_payment_note is not None:
            self.min_pos_payment_note = min_pos_payment_note
        if limit_lines_per_head_x is not None:
            self.limit_lines_per_head_x = limit_lines_per_head_x
        if min_pos_payment_note_x is not None:
            self.min_pos_payment_note_x = min_pos_payment_note_x
        if tenant is not None:
            self.tenant = tenant

    @property
    def code(self):
        """Gets the code of this PaymentmethodsBody.  # noqa: E501

        The code of the payment method  # noqa: E501

        :return: The code of this PaymentmethodsBody.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this PaymentmethodsBody.

        The code of the payment method  # noqa: E501

        :param code: The code of this PaymentmethodsBody.  # noqa: E501
        :type: str
        """

        self._code = code

    @property
    def description(self):
        """Gets the description of this PaymentmethodsBody.  # noqa: E501

        The description of the payment method  # noqa: E501

        :return: The description of this PaymentmethodsBody.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this PaymentmethodsBody.

        The description of the payment method  # noqa: E501

        :param description: The description of this PaymentmethodsBody.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def bal_account_type(self):
        """Gets the bal_account_type of this PaymentmethodsBody.  # noqa: E501

        The balance account type of the payment method  # noqa: E501

        :return: The bal_account_type of this PaymentmethodsBody.  # noqa: E501
        :rtype: str
        """
        return self._bal_account_type

    @bal_account_type.setter
    def bal_account_type(self, bal_account_type):
        """Sets the bal_account_type of this PaymentmethodsBody.

        The balance account type of the payment method  # noqa: E501

        :param bal_account_type: The bal_account_type of this PaymentmethodsBody.  # noqa: E501
        :type: str
        """

        self._bal_account_type = bal_account_type

    @property
    def bal_account_no(self):
        """Gets the bal_account_no of this PaymentmethodsBody.  # noqa: E501

        The balance account number of the payment method  # noqa: E501

        :return: The bal_account_no of this PaymentmethodsBody.  # noqa: E501
        :rtype: str
        """
        return self._bal_account_no

    @bal_account_no.setter
    def bal_account_no(self, bal_account_no):
        """Sets the bal_account_no of this PaymentmethodsBody.

        The balance account number of the payment method  # noqa: E501

        :param bal_account_no: The bal_account_no of this PaymentmethodsBody.  # noqa: E501
        :type: str
        """

        self._bal_account_no = bal_account_no

    @property
    def surcharge_variable(self):
        """Gets the surcharge_variable of this PaymentmethodsBody.  # noqa: E501

        The surcharge percentage (variable) of the payment method  # noqa: E501

        :return: The surcharge_variable of this PaymentmethodsBody.  # noqa: E501
        :rtype: str
        """
        return self._surcharge_variable

    @surcharge_variable.setter
    def surcharge_variable(self, surcharge_variable):
        """Sets the surcharge_variable of this PaymentmethodsBody.

        The surcharge percentage (variable) of the payment method  # noqa: E501

        :param surcharge_variable: The surcharge_variable of this PaymentmethodsBody.  # noqa: E501
        :type: str
        """

        self._surcharge_variable = surcharge_variable

    @property
    def surcharge_fix(self):
        """Gets the surcharge_fix of this PaymentmethodsBody.  # noqa: E501

        The surcharge amount (fixed) of the payment method  # noqa: E501

        :return: The surcharge_fix of this PaymentmethodsBody.  # noqa: E501
        :rtype: str
        """
        return self._surcharge_fix

    @surcharge_fix.setter
    def surcharge_fix(self, surcharge_fix):
        """Sets the surcharge_fix of this PaymentmethodsBody.

        The surcharge amount (fixed) of the payment method  # noqa: E501

        :param surcharge_fix: The surcharge_fix of this PaymentmethodsBody.  # noqa: E501
        :type: str
        """

        self._surcharge_fix = surcharge_fix

    @property
    def cutoff_amount_variable(self):
        """Gets the cutoff_amount_variable of this PaymentmethodsBody.  # noqa: E501

        The cutoff amount (variable) of the payment method  # noqa: E501

        :return: The cutoff_amount_variable of this PaymentmethodsBody.  # noqa: E501
        :rtype: str
        """
        return self._cutoff_amount_variable

    @cutoff_amount_variable.setter
    def cutoff_amount_variable(self, cutoff_amount_variable):
        """Sets the cutoff_amount_variable of this PaymentmethodsBody.

        The cutoff amount (variable) of the payment method  # noqa: E501

        :param cutoff_amount_variable: The cutoff_amount_variable of this PaymentmethodsBody.  # noqa: E501
        :type: str
        """

        self._cutoff_amount_variable = cutoff_amount_variable

    @property
    def fee_account(self):
        """Gets the fee_account of this PaymentmethodsBody.  # noqa: E501

        The fee account of the payment method  # noqa: E501

        :return: The fee_account of this PaymentmethodsBody.  # noqa: E501
        :rtype: str
        """
        return self._fee_account

    @fee_account.setter
    def fee_account(self, fee_account):
        """Sets the fee_account of this PaymentmethodsBody.

        The fee account of the payment method  # noqa: E501

        :param fee_account: The fee_account of this PaymentmethodsBody.  # noqa: E501
        :type: str
        """

        self._fee_account = fee_account

    @property
    def pay_view_code(self):
        """Gets the pay_view_code of this PaymentmethodsBody.  # noqa: E501

        The pay view code of the payment method  # noqa: E501

        :return: The pay_view_code of this PaymentmethodsBody.  # noqa: E501
        :rtype: str
        """
        return self._pay_view_code

    @pay_view_code.setter
    def pay_view_code(self, pay_view_code):
        """Sets the pay_view_code of this PaymentmethodsBody.

        The pay view code of the payment method  # noqa: E501

        :param pay_view_code: The pay_view_code of this PaymentmethodsBody.  # noqa: E501
        :type: str
        """

        self._pay_view_code = pay_view_code

    @property
    def cutoff_amount_fee(self):
        """Gets the cutoff_amount_fee of this PaymentmethodsBody.  # noqa: E501

        The cutoff amount for fee of the payment method  # noqa: E501

        :return: The cutoff_amount_fee of this PaymentmethodsBody.  # noqa: E501
        :rtype: str
        """
        return self._cutoff_amount_fee

    @cutoff_amount_fee.setter
    def cutoff_amount_fee(self, cutoff_amount_fee):
        """Sets the cutoff_amount_fee of this PaymentmethodsBody.

        The cutoff amount for fee of the payment method  # noqa: E501

        :param cutoff_amount_fee: The cutoff_amount_fee of this PaymentmethodsBody.  # noqa: E501
        :type: str
        """

        self._cutoff_amount_fee = cutoff_amount_fee

    @property
    def default_payment_type_code(self):
        """Gets the default_payment_type_code of this PaymentmethodsBody.  # noqa: E501

        The default payment type code of the payment method  # noqa: E501

        :return: The default_payment_type_code of this PaymentmethodsBody.  # noqa: E501
        :rtype: str
        """
        return self._default_payment_type_code

    @default_payment_type_code.setter
    def default_payment_type_code(self, default_payment_type_code):
        """Sets the default_payment_type_code of this PaymentmethodsBody.

        The default payment type code of the payment method  # noqa: E501

        :param default_payment_type_code: The default_payment_type_code of this PaymentmethodsBody.  # noqa: E501
        :type: str
        """

        self._default_payment_type_code = default_payment_type_code

    @property
    def single_payment(self):
        """Gets the single_payment of this PaymentmethodsBody.  # noqa: E501

        Indicates if single payment is enabled or not  # noqa: E501

        :return: The single_payment of this PaymentmethodsBody.  # noqa: E501
        :rtype: str
        """
        return self._single_payment

    @single_payment.setter
    def single_payment(self, single_payment):
        """Sets the single_payment of this PaymentmethodsBody.

        Indicates if single payment is enabled or not  # noqa: E501

        :param single_payment: The single_payment of this PaymentmethodsBody.  # noqa: E501
        :type: str
        """

        self._single_payment = single_payment

    @property
    def default_pmt_bank_account_no(self):
        """Gets the default_pmt_bank_account_no of this PaymentmethodsBody.  # noqa: E501

        The default payment bank account number of the payment method  # noqa: E501

        :return: The default_pmt_bank_account_no of this PaymentmethodsBody.  # noqa: E501
        :rtype: str
        """
        return self._default_pmt_bank_account_no

    @default_pmt_bank_account_no.setter
    def default_pmt_bank_account_no(self, default_pmt_bank_account_no):
        """Sets the default_pmt_bank_account_no of this PaymentmethodsBody.

        The default payment bank account number of the payment method  # noqa: E501

        :param default_pmt_bank_account_no: The default_pmt_bank_account_no of this PaymentmethodsBody.  # noqa: E501
        :type: str
        """

        self._default_pmt_bank_account_no = default_pmt_bank_account_no

    @property
    def separate_pmt_proposal_head(self):
        """Gets the separate_pmt_proposal_head of this PaymentmethodsBody.  # noqa: E501

        Indicates if separate payment proposal head is enabled or not  # noqa: E501

        :return: The separate_pmt_proposal_head of this PaymentmethodsBody.  # noqa: E501
        :rtype: str
        """
        return self._separate_pmt_proposal_head

    @separate_pmt_proposal_head.setter
    def separate_pmt_proposal_head(self, separate_pmt_proposal_head):
        """Sets the separate_pmt_proposal_head of this PaymentmethodsBody.

        Indicates if separate payment proposal head is enabled or not  # noqa: E501

        :param separate_pmt_proposal_head: The separate_pmt_proposal_head of this PaymentmethodsBody.  # noqa: E501
        :type: str
        """

        self._separate_pmt_proposal_head = separate_pmt_proposal_head

    @property
    def vendor_purpose_text(self):
        """Gets the vendor_purpose_text of this PaymentmethodsBody.  # noqa: E501

        The vendor purpose text of the payment method  # noqa: E501

        :return: The vendor_purpose_text of this PaymentmethodsBody.  # noqa: E501
        :rtype: str
        """
        return self._vendor_purpose_text

    @vendor_purpose_text.setter
    def vendor_purpose_text(self, vendor_purpose_text):
        """Sets the vendor_purpose_text of this PaymentmethodsBody.

        The vendor purpose text of the payment method  # noqa: E501

        :param vendor_purpose_text: The vendor_purpose_text of this PaymentmethodsBody.  # noqa: E501
        :type: str
        """

        self._vendor_purpose_text = vendor_purpose_text

    @property
    def customer_purpose_text(self):
        """Gets the customer_purpose_text of this PaymentmethodsBody.  # noqa: E501

        The customer purpose text of the payment method  # noqa: E501

        :return: The customer_purpose_text of this PaymentmethodsBody.  # noqa: E501
        :rtype: str
        """
        return self._customer_purpose_text

    @customer_purpose_text.setter
    def customer_purpose_text(self, customer_purpose_text):
        """Sets the customer_purpose_text of this PaymentmethodsBody.

        The customer purpose text of the payment method  # noqa: E501

        :param customer_purpose_text: The customer_purpose_text of this PaymentmethodsBody.  # noqa: E501
        :type: str
        """

        self._customer_purpose_text = customer_purpose_text

    @property
    def payment_note_purpose_text(self):
        """Gets the payment_note_purpose_text of this PaymentmethodsBody.  # noqa: E501

        The payment note purpose text of the payment method  # noqa: E501

        :return: The payment_note_purpose_text of this PaymentmethodsBody.  # noqa: E501
        :rtype: str
        """
        return self._payment_note_purpose_text

    @payment_note_purpose_text.setter
    def payment_note_purpose_text(self, payment_note_purpose_text):
        """Sets the payment_note_purpose_text of this PaymentmethodsBody.

        The payment note purpose text of the payment method  # noqa: E501

        :param payment_note_purpose_text: The payment_note_purpose_text of this PaymentmethodsBody.  # noqa: E501
        :type: str
        """

        self._payment_note_purpose_text = payment_note_purpose_text

    @property
    def vendor_purpose_text_header(self):
        """Gets the vendor_purpose_text_header of this PaymentmethodsBody.  # noqa: E501

        The vendor purpose text header of the payment method  # noqa: E501

        :return: The vendor_purpose_text_header of this PaymentmethodsBody.  # noqa: E501
        :rtype: str
        """
        return self._vendor_purpose_text_header

    @vendor_purpose_text_header.setter
    def vendor_purpose_text_header(self, vendor_purpose_text_header):
        """Sets the vendor_purpose_text_header of this PaymentmethodsBody.

        The vendor purpose text header of the payment method  # noqa: E501

        :param vendor_purpose_text_header: The vendor_purpose_text_header of this PaymentmethodsBody.  # noqa: E501
        :type: str
        """

        self._vendor_purpose_text_header = vendor_purpose_text_header

    @property
    def purpose_text_footer(self):
        """Gets the purpose_text_footer of this PaymentmethodsBody.  # noqa: E501

        The purpose text footer of the payment method  # noqa: E501

        :return: The purpose_text_footer of this PaymentmethodsBody.  # noqa: E501
        :rtype: str
        """
        return self._purpose_text_footer

    @purpose_text_footer.setter
    def purpose_text_footer(self, purpose_text_footer):
        """Sets the purpose_text_footer of this PaymentmethodsBody.

        The purpose text footer of the payment method  # noqa: E501

        :param purpose_text_footer: The purpose_text_footer of this PaymentmethodsBody.  # noqa: E501
        :type: str
        """

        self._purpose_text_footer = purpose_text_footer

    @property
    def limit_payment_amount_lcy(self):
        """Gets the limit_payment_amount_lcy of this PaymentmethodsBody.  # noqa: E501

        The limit payment amount in local currency of the payment method  # noqa: E501

        :return: The limit_payment_amount_lcy of this PaymentmethodsBody.  # noqa: E501
        :rtype: str
        """
        return self._limit_payment_amount_lcy

    @limit_payment_amount_lcy.setter
    def limit_payment_amount_lcy(self, limit_payment_amount_lcy):
        """Sets the limit_payment_amount_lcy of this PaymentmethodsBody.

        The limit payment amount in local currency of the payment method  # noqa: E501

        :param limit_payment_amount_lcy: The limit_payment_amount_lcy of this PaymentmethodsBody.  # noqa: E501
        :type: str
        """

        self._limit_payment_amount_lcy = limit_payment_amount_lcy

    @property
    def customer_purpose_text_header(self):
        """Gets the customer_purpose_text_header of this PaymentmethodsBody.  # noqa: E501

        The customer purpose text header of the payment method  # noqa: E501

        :return: The customer_purpose_text_header of this PaymentmethodsBody.  # noqa: E501
        :rtype: str
        """
        return self._customer_purpose_text_header

    @customer_purpose_text_header.setter
    def customer_purpose_text_header(self, customer_purpose_text_header):
        """Sets the customer_purpose_text_header of this PaymentmethodsBody.

        The customer purpose text header of the payment method  # noqa: E501

        :param customer_purpose_text_header: The customer_purpose_text_header of this PaymentmethodsBody.  # noqa: E501
        :type: str
        """

        self._customer_purpose_text_header = customer_purpose_text_header

    @property
    def limit_lines_per_head(self):
        """Gets the limit_lines_per_head of this PaymentmethodsBody.  # noqa: E501

        The limit lines per head of the payment method  # noqa: E501

        :return: The limit_lines_per_head of this PaymentmethodsBody.  # noqa: E501
        :rtype: str
        """
        return self._limit_lines_per_head

    @limit_lines_per_head.setter
    def limit_lines_per_head(self, limit_lines_per_head):
        """Sets the limit_lines_per_head of this PaymentmethodsBody.

        The limit lines per head of the payment method  # noqa: E501

        :param limit_lines_per_head: The limit_lines_per_head of this PaymentmethodsBody.  # noqa: E501
        :type: str
        """

        self._limit_lines_per_head = limit_lines_per_head

    @property
    def min_pos_payment_note(self):
        """Gets the min_pos_payment_note of this PaymentmethodsBody.  # noqa: E501

        The minimum positive payment note of the payment method  # noqa: E501

        :return: The min_pos_payment_note of this PaymentmethodsBody.  # noqa: E501
        :rtype: str
        """
        return self._min_pos_payment_note

    @min_pos_payment_note.setter
    def min_pos_payment_note(self, min_pos_payment_note):
        """Sets the min_pos_payment_note of this PaymentmethodsBody.

        The minimum positive payment note of the payment method  # noqa: E501

        :param min_pos_payment_note: The min_pos_payment_note of this PaymentmethodsBody.  # noqa: E501
        :type: str
        """

        self._min_pos_payment_note = min_pos_payment_note

    @property
    def limit_lines_per_head_x(self):
        """Gets the limit_lines_per_head_x of this PaymentmethodsBody.  # noqa: E501

        The limit lines per head X of the payment method  # noqa: E501

        :return: The limit_lines_per_head_x of this PaymentmethodsBody.  # noqa: E501
        :rtype: str
        """
        return self._limit_lines_per_head_x

    @limit_lines_per_head_x.setter
    def limit_lines_per_head_x(self, limit_lines_per_head_x):
        """Sets the limit_lines_per_head_x of this PaymentmethodsBody.

        The limit lines per head X of the payment method  # noqa: E501

        :param limit_lines_per_head_x: The limit_lines_per_head_x of this PaymentmethodsBody.  # noqa: E501
        :type: str
        """

        self._limit_lines_per_head_x = limit_lines_per_head_x

    @property
    def min_pos_payment_note_x(self):
        """Gets the min_pos_payment_note_x of this PaymentmethodsBody.  # noqa: E501

        The minimum positive payment note X of the payment method  # noqa: E501

        :return: The min_pos_payment_note_x of this PaymentmethodsBody.  # noqa: E501
        :rtype: str
        """
        return self._min_pos_payment_note_x

    @min_pos_payment_note_x.setter
    def min_pos_payment_note_x(self, min_pos_payment_note_x):
        """Sets the min_pos_payment_note_x of this PaymentmethodsBody.

        The minimum positive payment note X of the payment method  # noqa: E501

        :param min_pos_payment_note_x: The min_pos_payment_note_x of this PaymentmethodsBody.  # noqa: E501
        :type: str
        """

        self._min_pos_payment_note_x = min_pos_payment_note_x

    @property
    def tenant(self):
        """Gets the tenant of this PaymentmethodsBody.  # noqa: E501

        The tenant name  # noqa: E501

        :return: The tenant of this PaymentmethodsBody.  # noqa: E501
        :rtype: str
        """
        return self._tenant

    @tenant.setter
    def tenant(self, tenant):
        """Sets the tenant of this PaymentmethodsBody.

        The tenant name  # noqa: E501

        :param tenant: The tenant of this PaymentmethodsBody.  # noqa: E501
        :type: str
        """

        self._tenant = tenant

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(PaymentmethodsBody, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, PaymentmethodsBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
