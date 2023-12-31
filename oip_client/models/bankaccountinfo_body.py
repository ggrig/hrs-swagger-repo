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

class BankaccountinfoBody(object):
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
        'mandate_id': 'str',
        'auto_pay_enabled': 'bool',
        'customer_no': 'str',
        'iban': 'str',
        'swift_code': 'str',
        'owner': 'str',
        'company': 'str'
    }

    attribute_map = {
        'mandate_id': 'MandateID',
        'auto_pay_enabled': 'AutoPayEnabled',
        'customer_no': 'CustomerNo',
        'iban': 'IBAN',
        'swift_code': 'SWIFTCode',
        'owner': 'Owner',
        'company': 'Company'
    }

    def __init__(self, mandate_id=None, auto_pay_enabled=None, customer_no=None, iban=None, swift_code=None, owner=None, company=None):  # noqa: E501
        """BankaccountinfoBody - a model defined in Swagger"""  # noqa: E501
        self._mandate_id = None
        self._auto_pay_enabled = None
        self._customer_no = None
        self._iban = None
        self._swift_code = None
        self._owner = None
        self._company = None
        self.discriminator = None
        if mandate_id is not None:
            self.mandate_id = mandate_id
        if auto_pay_enabled is not None:
            self.auto_pay_enabled = auto_pay_enabled
        if customer_no is not None:
            self.customer_no = customer_no
        if iban is not None:
            self.iban = iban
        if swift_code is not None:
            self.swift_code = swift_code
        if owner is not None:
            self.owner = owner
        if company is not None:
            self.company = company

    @property
    def mandate_id(self):
        """Gets the mandate_id of this BankaccountinfoBody.  # noqa: E501

        The Mandate ID  # noqa: E501

        :return: The mandate_id of this BankaccountinfoBody.  # noqa: E501
        :rtype: str
        """
        return self._mandate_id

    @mandate_id.setter
    def mandate_id(self, mandate_id):
        """Sets the mandate_id of this BankaccountinfoBody.

        The Mandate ID  # noqa: E501

        :param mandate_id: The mandate_id of this BankaccountinfoBody.  # noqa: E501
        :type: str
        """

        self._mandate_id = mandate_id

    @property
    def auto_pay_enabled(self):
        """Gets the auto_pay_enabled of this BankaccountinfoBody.  # noqa: E501

        Indicates if autopay is enabled  # noqa: E501

        :return: The auto_pay_enabled of this BankaccountinfoBody.  # noqa: E501
        :rtype: bool
        """
        return self._auto_pay_enabled

    @auto_pay_enabled.setter
    def auto_pay_enabled(self, auto_pay_enabled):
        """Sets the auto_pay_enabled of this BankaccountinfoBody.

        Indicates if autopay is enabled  # noqa: E501

        :param auto_pay_enabled: The auto_pay_enabled of this BankaccountinfoBody.  # noqa: E501
        :type: bool
        """

        self._auto_pay_enabled = auto_pay_enabled

    @property
    def customer_no(self):
        """Gets the customer_no of this BankaccountinfoBody.  # noqa: E501

        The Customer Number  # noqa: E501

        :return: The customer_no of this BankaccountinfoBody.  # noqa: E501
        :rtype: str
        """
        return self._customer_no

    @customer_no.setter
    def customer_no(self, customer_no):
        """Sets the customer_no of this BankaccountinfoBody.

        The Customer Number  # noqa: E501

        :param customer_no: The customer_no of this BankaccountinfoBody.  # noqa: E501
        :type: str
        """

        self._customer_no = customer_no

    @property
    def iban(self):
        """Gets the iban of this BankaccountinfoBody.  # noqa: E501

        The IBAN  # noqa: E501

        :return: The iban of this BankaccountinfoBody.  # noqa: E501
        :rtype: str
        """
        return self._iban

    @iban.setter
    def iban(self, iban):
        """Sets the iban of this BankaccountinfoBody.

        The IBAN  # noqa: E501

        :param iban: The iban of this BankaccountinfoBody.  # noqa: E501
        :type: str
        """

        self._iban = iban

    @property
    def swift_code(self):
        """Gets the swift_code of this BankaccountinfoBody.  # noqa: E501

        The SWIFT Code  # noqa: E501

        :return: The swift_code of this BankaccountinfoBody.  # noqa: E501
        :rtype: str
        """
        return self._swift_code

    @swift_code.setter
    def swift_code(self, swift_code):
        """Sets the swift_code of this BankaccountinfoBody.

        The SWIFT Code  # noqa: E501

        :param swift_code: The swift_code of this BankaccountinfoBody.  # noqa: E501
        :type: str
        """

        self._swift_code = swift_code

    @property
    def owner(self):
        """Gets the owner of this BankaccountinfoBody.  # noqa: E501

        The account owner  # noqa: E501

        :return: The owner of this BankaccountinfoBody.  # noqa: E501
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this BankaccountinfoBody.

        The account owner  # noqa: E501

        :param owner: The owner of this BankaccountinfoBody.  # noqa: E501
        :type: str
        """

        self._owner = owner

    @property
    def company(self):
        """Gets the company of this BankaccountinfoBody.  # noqa: E501

        The tenant name  # noqa: E501

        :return: The company of this BankaccountinfoBody.  # noqa: E501
        :rtype: str
        """
        return self._company

    @company.setter
    def company(self, company):
        """Sets the company of this BankaccountinfoBody.

        The tenant name  # noqa: E501

        :param company: The company of this BankaccountinfoBody.  # noqa: E501
        :type: str
        """

        self._company = company

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
        if issubclass(BankaccountinfoBody, dict):
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
        if not isinstance(other, BankaccountinfoBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
