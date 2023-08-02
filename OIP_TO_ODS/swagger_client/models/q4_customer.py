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

class Q4Customer(object):
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
        'customer_no': 'str',
        'name': 'str',
        'name2': 'str',
        'address': 'str',
        'address2': 'str',
        'city': 'str',
        'post_code': 'str',
        'country_region': 'str',
        'contact': 'str',
        'phone': 'str',
        'correspondence_type': 'str',
        'e_mail': 'str',
        'fax': 'str',
        'e_mail_copy': 'str',
        'fax_copy': 'str'
    }

    attribute_map = {
        'customer_no': 'CustomerNo',
        'name': 'Name',
        'name2': 'Name2',
        'address': 'Address',
        'address2': 'Address2',
        'city': 'City',
        'post_code': 'PostCode',
        'country_region': 'CountryRegion',
        'contact': 'Contact',
        'phone': 'Phone',
        'correspondence_type': 'CorrespondenceType',
        'e_mail': 'EMail',
        'fax': 'Fax',
        'e_mail_copy': 'EMailCopy',
        'fax_copy': 'FaxCopy'
    }

    def __init__(self, customer_no=None, name=None, name2=None, address=None, address2=None, city=None, post_code=None, country_region=None, contact=None, phone=None, correspondence_type=None, e_mail=None, fax=None, e_mail_copy=None, fax_copy=None):  # noqa: E501
        """Q4Customer - a model defined in Swagger"""  # noqa: E501
        self._customer_no = None
        self._name = None
        self._name2 = None
        self._address = None
        self._address2 = None
        self._city = None
        self._post_code = None
        self._country_region = None
        self._contact = None
        self._phone = None
        self._correspondence_type = None
        self._e_mail = None
        self._fax = None
        self._e_mail_copy = None
        self._fax_copy = None
        self.discriminator = None
        self.customer_no = customer_no
        self.name = name
        self.name2 = name2
        self.address = address
        self.address2 = address2
        self.city = city
        self.post_code = post_code
        self.country_region = country_region
        self.contact = contact
        self.phone = phone
        self.correspondence_type = correspondence_type
        self.e_mail = e_mail
        self.fax = fax
        self.e_mail_copy = e_mail_copy
        self.fax_copy = fax_copy

    @property
    def customer_no(self):
        """Gets the customer_no of this Q4Customer.  # noqa: E501


        :return: The customer_no of this Q4Customer.  # noqa: E501
        :rtype: str
        """
        return self._customer_no

    @customer_no.setter
    def customer_no(self, customer_no):
        """Sets the customer_no of this Q4Customer.


        :param customer_no: The customer_no of this Q4Customer.  # noqa: E501
        :type: str
        """
        if customer_no is None:
            raise ValueError("Invalid value for `customer_no`, must not be `None`")  # noqa: E501

        self._customer_no = customer_no

    @property
    def name(self):
        """Gets the name of this Q4Customer.  # noqa: E501


        :return: The name of this Q4Customer.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Q4Customer.


        :param name: The name of this Q4Customer.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def name2(self):
        """Gets the name2 of this Q4Customer.  # noqa: E501


        :return: The name2 of this Q4Customer.  # noqa: E501
        :rtype: str
        """
        return self._name2

    @name2.setter
    def name2(self, name2):
        """Sets the name2 of this Q4Customer.


        :param name2: The name2 of this Q4Customer.  # noqa: E501
        :type: str
        """
        if name2 is None:
            raise ValueError("Invalid value for `name2`, must not be `None`")  # noqa: E501

        self._name2 = name2

    @property
    def address(self):
        """Gets the address of this Q4Customer.  # noqa: E501


        :return: The address of this Q4Customer.  # noqa: E501
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this Q4Customer.


        :param address: The address of this Q4Customer.  # noqa: E501
        :type: str
        """
        if address is None:
            raise ValueError("Invalid value for `address`, must not be `None`")  # noqa: E501

        self._address = address

    @property
    def address2(self):
        """Gets the address2 of this Q4Customer.  # noqa: E501


        :return: The address2 of this Q4Customer.  # noqa: E501
        :rtype: str
        """
        return self._address2

    @address2.setter
    def address2(self, address2):
        """Sets the address2 of this Q4Customer.


        :param address2: The address2 of this Q4Customer.  # noqa: E501
        :type: str
        """
        if address2 is None:
            raise ValueError("Invalid value for `address2`, must not be `None`")  # noqa: E501

        self._address2 = address2

    @property
    def city(self):
        """Gets the city of this Q4Customer.  # noqa: E501


        :return: The city of this Q4Customer.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this Q4Customer.


        :param city: The city of this Q4Customer.  # noqa: E501
        :type: str
        """
        if city is None:
            raise ValueError("Invalid value for `city`, must not be `None`")  # noqa: E501

        self._city = city

    @property
    def post_code(self):
        """Gets the post_code of this Q4Customer.  # noqa: E501


        :return: The post_code of this Q4Customer.  # noqa: E501
        :rtype: str
        """
        return self._post_code

    @post_code.setter
    def post_code(self, post_code):
        """Sets the post_code of this Q4Customer.


        :param post_code: The post_code of this Q4Customer.  # noqa: E501
        :type: str
        """
        if post_code is None:
            raise ValueError("Invalid value for `post_code`, must not be `None`")  # noqa: E501

        self._post_code = post_code

    @property
    def country_region(self):
        """Gets the country_region of this Q4Customer.  # noqa: E501


        :return: The country_region of this Q4Customer.  # noqa: E501
        :rtype: str
        """
        return self._country_region

    @country_region.setter
    def country_region(self, country_region):
        """Sets the country_region of this Q4Customer.


        :param country_region: The country_region of this Q4Customer.  # noqa: E501
        :type: str
        """
        if country_region is None:
            raise ValueError("Invalid value for `country_region`, must not be `None`")  # noqa: E501

        self._country_region = country_region

    @property
    def contact(self):
        """Gets the contact of this Q4Customer.  # noqa: E501


        :return: The contact of this Q4Customer.  # noqa: E501
        :rtype: str
        """
        return self._contact

    @contact.setter
    def contact(self, contact):
        """Sets the contact of this Q4Customer.


        :param contact: The contact of this Q4Customer.  # noqa: E501
        :type: str
        """
        if contact is None:
            raise ValueError("Invalid value for `contact`, must not be `None`")  # noqa: E501

        self._contact = contact

    @property
    def phone(self):
        """Gets the phone of this Q4Customer.  # noqa: E501


        :return: The phone of this Q4Customer.  # noqa: E501
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this Q4Customer.


        :param phone: The phone of this Q4Customer.  # noqa: E501
        :type: str
        """
        if phone is None:
            raise ValueError("Invalid value for `phone`, must not be `None`")  # noqa: E501

        self._phone = phone

    @property
    def correspondence_type(self):
        """Gets the correspondence_type of this Q4Customer.  # noqa: E501


        :return: The correspondence_type of this Q4Customer.  # noqa: E501
        :rtype: str
        """
        return self._correspondence_type

    @correspondence_type.setter
    def correspondence_type(self, correspondence_type):
        """Sets the correspondence_type of this Q4Customer.


        :param correspondence_type: The correspondence_type of this Q4Customer.  # noqa: E501
        :type: str
        """
        if correspondence_type is None:
            raise ValueError("Invalid value for `correspondence_type`, must not be `None`")  # noqa: E501

        self._correspondence_type = correspondence_type

    @property
    def e_mail(self):
        """Gets the e_mail of this Q4Customer.  # noqa: E501


        :return: The e_mail of this Q4Customer.  # noqa: E501
        :rtype: str
        """
        return self._e_mail

    @e_mail.setter
    def e_mail(self, e_mail):
        """Sets the e_mail of this Q4Customer.


        :param e_mail: The e_mail of this Q4Customer.  # noqa: E501
        :type: str
        """
        if e_mail is None:
            raise ValueError("Invalid value for `e_mail`, must not be `None`")  # noqa: E501

        self._e_mail = e_mail

    @property
    def fax(self):
        """Gets the fax of this Q4Customer.  # noqa: E501


        :return: The fax of this Q4Customer.  # noqa: E501
        :rtype: str
        """
        return self._fax

    @fax.setter
    def fax(self, fax):
        """Sets the fax of this Q4Customer.


        :param fax: The fax of this Q4Customer.  # noqa: E501
        :type: str
        """
        if fax is None:
            raise ValueError("Invalid value for `fax`, must not be `None`")  # noqa: E501

        self._fax = fax

    @property
    def e_mail_copy(self):
        """Gets the e_mail_copy of this Q4Customer.  # noqa: E501


        :return: The e_mail_copy of this Q4Customer.  # noqa: E501
        :rtype: str
        """
        return self._e_mail_copy

    @e_mail_copy.setter
    def e_mail_copy(self, e_mail_copy):
        """Sets the e_mail_copy of this Q4Customer.


        :param e_mail_copy: The e_mail_copy of this Q4Customer.  # noqa: E501
        :type: str
        """
        if e_mail_copy is None:
            raise ValueError("Invalid value for `e_mail_copy`, must not be `None`")  # noqa: E501

        self._e_mail_copy = e_mail_copy

    @property
    def fax_copy(self):
        """Gets the fax_copy of this Q4Customer.  # noqa: E501


        :return: The fax_copy of this Q4Customer.  # noqa: E501
        :rtype: str
        """
        return self._fax_copy

    @fax_copy.setter
    def fax_copy(self, fax_copy):
        """Sets the fax_copy of this Q4Customer.


        :param fax_copy: The fax_copy of this Q4Customer.  # noqa: E501
        :type: str
        """
        if fax_copy is None:
            raise ValueError("Invalid value for `fax_copy`, must not be `None`")  # noqa: E501

        self._fax_copy = fax_copy

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
        if issubclass(Q4Customer, dict):
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
        if not isinstance(other, Q4Customer):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
