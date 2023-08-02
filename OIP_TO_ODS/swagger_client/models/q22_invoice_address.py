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

class Q22InvoiceAddress(object):
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
        'address': 'str',
        'address2': 'str',
        'city': 'str',
        'customer_no': 'str',
        'name': 'str',
        'name2': 'str',
        'post_code': 'str',
        'country_code': 'str',
        'correspondence_type': 'str',
        'correspondence_address': 'str',
        'accounting_contact': 'str'
    }

    attribute_map = {
        'address': 'Address',
        'address2': 'Address2',
        'city': 'City',
        'customer_no': 'CustomerNo',
        'name': 'Name',
        'name2': 'Name2',
        'post_code': 'PostCode',
        'country_code': 'CountryCode',
        'correspondence_type': 'CorrespondenceType',
        'correspondence_address': 'CorrespondenceAddress',
        'accounting_contact': 'AccountingContact'
    }

    def __init__(self, address=None, address2=None, city=None, customer_no=None, name=None, name2=None, post_code=None, country_code=None, correspondence_type=None, correspondence_address=None, accounting_contact=None):  # noqa: E501
        """Q22InvoiceAddress - a model defined in Swagger"""  # noqa: E501
        self._address = None
        self._address2 = None
        self._city = None
        self._customer_no = None
        self._name = None
        self._name2 = None
        self._post_code = None
        self._country_code = None
        self._correspondence_type = None
        self._correspondence_address = None
        self._accounting_contact = None
        self.discriminator = None
        self.address = address
        self.address2 = address2
        self.city = city
        self.customer_no = customer_no
        self.name = name
        self.name2 = name2
        self.post_code = post_code
        self.country_code = country_code
        self.correspondence_type = correspondence_type
        self.correspondence_address = correspondence_address
        self.accounting_contact = accounting_contact

    @property
    def address(self):
        """Gets the address of this Q22InvoiceAddress.  # noqa: E501


        :return: The address of this Q22InvoiceAddress.  # noqa: E501
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this Q22InvoiceAddress.


        :param address: The address of this Q22InvoiceAddress.  # noqa: E501
        :type: str
        """
        if address is None:
            raise ValueError("Invalid value for `address`, must not be `None`")  # noqa: E501

        self._address = address

    @property
    def address2(self):
        """Gets the address2 of this Q22InvoiceAddress.  # noqa: E501


        :return: The address2 of this Q22InvoiceAddress.  # noqa: E501
        :rtype: str
        """
        return self._address2

    @address2.setter
    def address2(self, address2):
        """Sets the address2 of this Q22InvoiceAddress.


        :param address2: The address2 of this Q22InvoiceAddress.  # noqa: E501
        :type: str
        """
        if address2 is None:
            raise ValueError("Invalid value for `address2`, must not be `None`")  # noqa: E501

        self._address2 = address2

    @property
    def city(self):
        """Gets the city of this Q22InvoiceAddress.  # noqa: E501


        :return: The city of this Q22InvoiceAddress.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this Q22InvoiceAddress.


        :param city: The city of this Q22InvoiceAddress.  # noqa: E501
        :type: str
        """
        if city is None:
            raise ValueError("Invalid value for `city`, must not be `None`")  # noqa: E501

        self._city = city

    @property
    def customer_no(self):
        """Gets the customer_no of this Q22InvoiceAddress.  # noqa: E501


        :return: The customer_no of this Q22InvoiceAddress.  # noqa: E501
        :rtype: str
        """
        return self._customer_no

    @customer_no.setter
    def customer_no(self, customer_no):
        """Sets the customer_no of this Q22InvoiceAddress.


        :param customer_no: The customer_no of this Q22InvoiceAddress.  # noqa: E501
        :type: str
        """
        if customer_no is None:
            raise ValueError("Invalid value for `customer_no`, must not be `None`")  # noqa: E501

        self._customer_no = customer_no

    @property
    def name(self):
        """Gets the name of this Q22InvoiceAddress.  # noqa: E501


        :return: The name of this Q22InvoiceAddress.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Q22InvoiceAddress.


        :param name: The name of this Q22InvoiceAddress.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def name2(self):
        """Gets the name2 of this Q22InvoiceAddress.  # noqa: E501


        :return: The name2 of this Q22InvoiceAddress.  # noqa: E501
        :rtype: str
        """
        return self._name2

    @name2.setter
    def name2(self, name2):
        """Sets the name2 of this Q22InvoiceAddress.


        :param name2: The name2 of this Q22InvoiceAddress.  # noqa: E501
        :type: str
        """
        if name2 is None:
            raise ValueError("Invalid value for `name2`, must not be `None`")  # noqa: E501

        self._name2 = name2

    @property
    def post_code(self):
        """Gets the post_code of this Q22InvoiceAddress.  # noqa: E501


        :return: The post_code of this Q22InvoiceAddress.  # noqa: E501
        :rtype: str
        """
        return self._post_code

    @post_code.setter
    def post_code(self, post_code):
        """Sets the post_code of this Q22InvoiceAddress.


        :param post_code: The post_code of this Q22InvoiceAddress.  # noqa: E501
        :type: str
        """
        if post_code is None:
            raise ValueError("Invalid value for `post_code`, must not be `None`")  # noqa: E501

        self._post_code = post_code

    @property
    def country_code(self):
        """Gets the country_code of this Q22InvoiceAddress.  # noqa: E501


        :return: The country_code of this Q22InvoiceAddress.  # noqa: E501
        :rtype: str
        """
        return self._country_code

    @country_code.setter
    def country_code(self, country_code):
        """Sets the country_code of this Q22InvoiceAddress.


        :param country_code: The country_code of this Q22InvoiceAddress.  # noqa: E501
        :type: str
        """
        if country_code is None:
            raise ValueError("Invalid value for `country_code`, must not be `None`")  # noqa: E501

        self._country_code = country_code

    @property
    def correspondence_type(self):
        """Gets the correspondence_type of this Q22InvoiceAddress.  # noqa: E501


        :return: The correspondence_type of this Q22InvoiceAddress.  # noqa: E501
        :rtype: str
        """
        return self._correspondence_type

    @correspondence_type.setter
    def correspondence_type(self, correspondence_type):
        """Sets the correspondence_type of this Q22InvoiceAddress.


        :param correspondence_type: The correspondence_type of this Q22InvoiceAddress.  # noqa: E501
        :type: str
        """
        if correspondence_type is None:
            raise ValueError("Invalid value for `correspondence_type`, must not be `None`")  # noqa: E501

        self._correspondence_type = correspondence_type

    @property
    def correspondence_address(self):
        """Gets the correspondence_address of this Q22InvoiceAddress.  # noqa: E501


        :return: The correspondence_address of this Q22InvoiceAddress.  # noqa: E501
        :rtype: str
        """
        return self._correspondence_address

    @correspondence_address.setter
    def correspondence_address(self, correspondence_address):
        """Sets the correspondence_address of this Q22InvoiceAddress.


        :param correspondence_address: The correspondence_address of this Q22InvoiceAddress.  # noqa: E501
        :type: str
        """
        if correspondence_address is None:
            raise ValueError("Invalid value for `correspondence_address`, must not be `None`")  # noqa: E501

        self._correspondence_address = correspondence_address

    @property
    def accounting_contact(self):
        """Gets the accounting_contact of this Q22InvoiceAddress.  # noqa: E501


        :return: The accounting_contact of this Q22InvoiceAddress.  # noqa: E501
        :rtype: str
        """
        return self._accounting_contact

    @accounting_contact.setter
    def accounting_contact(self, accounting_contact):
        """Sets the accounting_contact of this Q22InvoiceAddress.


        :param accounting_contact: The accounting_contact of this Q22InvoiceAddress.  # noqa: E501
        :type: str
        """
        if accounting_contact is None:
            raise ValueError("Invalid value for `accounting_contact`, must not be `None`")  # noqa: E501

        self._accounting_contact = accounting_contact

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
        if issubclass(Q22InvoiceAddress, dict):
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
        if not isinstance(other, Q22InvoiceAddress):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
