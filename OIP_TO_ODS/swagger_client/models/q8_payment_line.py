# coding: utf-8

"""
    HPP

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class Q8PaymentLine(object):
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
        'posting_date': 'str',
        'payment_method_code': 'str',
        'ext_document_no': 'str',
        'documents': 'AllOfq8PaymentLineDocuments',
        'currency_code': 'str',
        'remaining_amount': 'str',
        'fix_fee_amount': 'str',
        'var_fee_amount': 'str'
    }

    attribute_map = {
        'posting_date': 'PostingDate',
        'payment_method_code': 'PaymentMethodCode',
        'ext_document_no': 'ExtDocumentNo',
        'documents': 'Documents',
        'currency_code': 'CurrencyCode',
        'remaining_amount': 'RemainingAmount',
        'fix_fee_amount': 'FixFeeAmount',
        'var_fee_amount': 'VarFeeAmount'
    }

    def __init__(self, posting_date=None, payment_method_code=None, ext_document_no=None, documents=None, currency_code=None, remaining_amount=None, fix_fee_amount=None, var_fee_amount=None):  # noqa: E501
        """Q8PaymentLine - a model defined in Swagger"""  # noqa: E501
        self._posting_date = None
        self._payment_method_code = None
        self._ext_document_no = None
        self._documents = None
        self._currency_code = None
        self._remaining_amount = None
        self._fix_fee_amount = None
        self._var_fee_amount = None
        self.discriminator = None
        self.posting_date = posting_date
        self.payment_method_code = payment_method_code
        self.ext_document_no = ext_document_no
        self.documents = documents
        self.currency_code = currency_code
        self.remaining_amount = remaining_amount
        self.fix_fee_amount = fix_fee_amount
        self.var_fee_amount = var_fee_amount

    @property
    def posting_date(self):
        """Gets the posting_date of this Q8PaymentLine.  # noqa: E501


        :return: The posting_date of this Q8PaymentLine.  # noqa: E501
        :rtype: str
        """
        return self._posting_date

    @posting_date.setter
    def posting_date(self, posting_date):
        """Sets the posting_date of this Q8PaymentLine.


        :param posting_date: The posting_date of this Q8PaymentLine.  # noqa: E501
        :type: str
        """
        if posting_date is None:
            raise ValueError("Invalid value for `posting_date`, must not be `None`")  # noqa: E501

        self._posting_date = posting_date

    @property
    def payment_method_code(self):
        """Gets the payment_method_code of this Q8PaymentLine.  # noqa: E501


        :return: The payment_method_code of this Q8PaymentLine.  # noqa: E501
        :rtype: str
        """
        return self._payment_method_code

    @payment_method_code.setter
    def payment_method_code(self, payment_method_code):
        """Sets the payment_method_code of this Q8PaymentLine.


        :param payment_method_code: The payment_method_code of this Q8PaymentLine.  # noqa: E501
        :type: str
        """
        if payment_method_code is None:
            raise ValueError("Invalid value for `payment_method_code`, must not be `None`")  # noqa: E501

        self._payment_method_code = payment_method_code

    @property
    def ext_document_no(self):
        """Gets the ext_document_no of this Q8PaymentLine.  # noqa: E501


        :return: The ext_document_no of this Q8PaymentLine.  # noqa: E501
        :rtype: str
        """
        return self._ext_document_no

    @ext_document_no.setter
    def ext_document_no(self, ext_document_no):
        """Sets the ext_document_no of this Q8PaymentLine.


        :param ext_document_no: The ext_document_no of this Q8PaymentLine.  # noqa: E501
        :type: str
        """
        if ext_document_no is None:
            raise ValueError("Invalid value for `ext_document_no`, must not be `None`")  # noqa: E501

        self._ext_document_no = ext_document_no

    @property
    def documents(self):
        """Gets the documents of this Q8PaymentLine.  # noqa: E501


        :return: The documents of this Q8PaymentLine.  # noqa: E501
        :rtype: AllOfq8PaymentLineDocuments
        """
        return self._documents

    @documents.setter
    def documents(self, documents):
        """Sets the documents of this Q8PaymentLine.


        :param documents: The documents of this Q8PaymentLine.  # noqa: E501
        :type: AllOfq8PaymentLineDocuments
        """
        if documents is None:
            raise ValueError("Invalid value for `documents`, must not be `None`")  # noqa: E501

        self._documents = documents

    @property
    def currency_code(self):
        """Gets the currency_code of this Q8PaymentLine.  # noqa: E501


        :return: The currency_code of this Q8PaymentLine.  # noqa: E501
        :rtype: str
        """
        return self._currency_code

    @currency_code.setter
    def currency_code(self, currency_code):
        """Sets the currency_code of this Q8PaymentLine.


        :param currency_code: The currency_code of this Q8PaymentLine.  # noqa: E501
        :type: str
        """
        if currency_code is None:
            raise ValueError("Invalid value for `currency_code`, must not be `None`")  # noqa: E501

        self._currency_code = currency_code

    @property
    def remaining_amount(self):
        """Gets the remaining_amount of this Q8PaymentLine.  # noqa: E501


        :return: The remaining_amount of this Q8PaymentLine.  # noqa: E501
        :rtype: str
        """
        return self._remaining_amount

    @remaining_amount.setter
    def remaining_amount(self, remaining_amount):
        """Sets the remaining_amount of this Q8PaymentLine.


        :param remaining_amount: The remaining_amount of this Q8PaymentLine.  # noqa: E501
        :type: str
        """
        if remaining_amount is None:
            raise ValueError("Invalid value for `remaining_amount`, must not be `None`")  # noqa: E501

        self._remaining_amount = remaining_amount

    @property
    def fix_fee_amount(self):
        """Gets the fix_fee_amount of this Q8PaymentLine.  # noqa: E501


        :return: The fix_fee_amount of this Q8PaymentLine.  # noqa: E501
        :rtype: str
        """
        return self._fix_fee_amount

    @fix_fee_amount.setter
    def fix_fee_amount(self, fix_fee_amount):
        """Sets the fix_fee_amount of this Q8PaymentLine.


        :param fix_fee_amount: The fix_fee_amount of this Q8PaymentLine.  # noqa: E501
        :type: str
        """
        if fix_fee_amount is None:
            raise ValueError("Invalid value for `fix_fee_amount`, must not be `None`")  # noqa: E501

        self._fix_fee_amount = fix_fee_amount

    @property
    def var_fee_amount(self):
        """Gets the var_fee_amount of this Q8PaymentLine.  # noqa: E501


        :return: The var_fee_amount of this Q8PaymentLine.  # noqa: E501
        :rtype: str
        """
        return self._var_fee_amount

    @var_fee_amount.setter
    def var_fee_amount(self, var_fee_amount):
        """Sets the var_fee_amount of this Q8PaymentLine.


        :param var_fee_amount: The var_fee_amount of this Q8PaymentLine.  # noqa: E501
        :type: str
        """
        if var_fee_amount is None:
            raise ValueError("Invalid value for `var_fee_amount`, must not be `None`")  # noqa: E501

        self._var_fee_amount = var_fee_amount

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
        if issubclass(Q8PaymentLine, dict):
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
        if not isinstance(other, Q8PaymentLine):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
