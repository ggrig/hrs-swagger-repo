# coding: utf-8

"""
    HPP-V2

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class Q6Contact(object):
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
        'contact_no': 'str',
        'first_name': 'str',
        'middle_name': 'str',
        'surname': 'str',
        'e_mail': 'str',
        'phone_no': 'str',
        'fax_no': 'str'
    }

    attribute_map = {
        'contact_no': 'ContactNo',
        'first_name': 'FirstName',
        'middle_name': 'MiddleName',
        'surname': 'Surname',
        'e_mail': 'EMail',
        'phone_no': 'PhoneNo',
        'fax_no': 'FaxNo'
    }

    def __init__(self, contact_no=None, first_name=None, middle_name=None, surname=None, e_mail=None, phone_no=None, fax_no=None):  # noqa: E501
        """Q6Contact - a model defined in Swagger"""  # noqa: E501
        self._contact_no = None
        self._first_name = None
        self._middle_name = None
        self._surname = None
        self._e_mail = None
        self._phone_no = None
        self._fax_no = None
        self.discriminator = None
        self.contact_no = contact_no
        self.first_name = first_name
        self.middle_name = middle_name
        self.surname = surname
        self.e_mail = e_mail
        self.phone_no = phone_no
        self.fax_no = fax_no

    @property
    def contact_no(self):
        """Gets the contact_no of this Q6Contact.  # noqa: E501


        :return: The contact_no of this Q6Contact.  # noqa: E501
        :rtype: str
        """
        return self._contact_no

    @contact_no.setter
    def contact_no(self, contact_no):
        """Sets the contact_no of this Q6Contact.


        :param contact_no: The contact_no of this Q6Contact.  # noqa: E501
        :type: str
        """
        if contact_no is None:
            raise ValueError("Invalid value for `contact_no`, must not be `None`")  # noqa: E501

        self._contact_no = contact_no

    @property
    def first_name(self):
        """Gets the first_name of this Q6Contact.  # noqa: E501


        :return: The first_name of this Q6Contact.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this Q6Contact.


        :param first_name: The first_name of this Q6Contact.  # noqa: E501
        :type: str
        """
        if first_name is None:
            raise ValueError("Invalid value for `first_name`, must not be `None`")  # noqa: E501

        self._first_name = first_name

    @property
    def middle_name(self):
        """Gets the middle_name of this Q6Contact.  # noqa: E501


        :return: The middle_name of this Q6Contact.  # noqa: E501
        :rtype: str
        """
        return self._middle_name

    @middle_name.setter
    def middle_name(self, middle_name):
        """Sets the middle_name of this Q6Contact.


        :param middle_name: The middle_name of this Q6Contact.  # noqa: E501
        :type: str
        """
        if middle_name is None:
            raise ValueError("Invalid value for `middle_name`, must not be `None`")  # noqa: E501

        self._middle_name = middle_name

    @property
    def surname(self):
        """Gets the surname of this Q6Contact.  # noqa: E501


        :return: The surname of this Q6Contact.  # noqa: E501
        :rtype: str
        """
        return self._surname

    @surname.setter
    def surname(self, surname):
        """Sets the surname of this Q6Contact.


        :param surname: The surname of this Q6Contact.  # noqa: E501
        :type: str
        """
        if surname is None:
            raise ValueError("Invalid value for `surname`, must not be `None`")  # noqa: E501

        self._surname = surname

    @property
    def e_mail(self):
        """Gets the e_mail of this Q6Contact.  # noqa: E501


        :return: The e_mail of this Q6Contact.  # noqa: E501
        :rtype: str
        """
        return self._e_mail

    @e_mail.setter
    def e_mail(self, e_mail):
        """Sets the e_mail of this Q6Contact.


        :param e_mail: The e_mail of this Q6Contact.  # noqa: E501
        :type: str
        """
        if e_mail is None:
            raise ValueError("Invalid value for `e_mail`, must not be `None`")  # noqa: E501

        self._e_mail = e_mail

    @property
    def phone_no(self):
        """Gets the phone_no of this Q6Contact.  # noqa: E501


        :return: The phone_no of this Q6Contact.  # noqa: E501
        :rtype: str
        """
        return self._phone_no

    @phone_no.setter
    def phone_no(self, phone_no):
        """Sets the phone_no of this Q6Contact.


        :param phone_no: The phone_no of this Q6Contact.  # noqa: E501
        :type: str
        """
        if phone_no is None:
            raise ValueError("Invalid value for `phone_no`, must not be `None`")  # noqa: E501

        self._phone_no = phone_no

    @property
    def fax_no(self):
        """Gets the fax_no of this Q6Contact.  # noqa: E501


        :return: The fax_no of this Q6Contact.  # noqa: E501
        :rtype: str
        """
        return self._fax_no

    @fax_no.setter
    def fax_no(self, fax_no):
        """Sets the fax_no of this Q6Contact.


        :param fax_no: The fax_no of this Q6Contact.  # noqa: E501
        :type: str
        """
        if fax_no is None:
            raise ValueError("Invalid value for `fax_no`, must not be `None`")  # noqa: E501

        self._fax_no = fax_no

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
        if issubclass(Q6Contact, dict):
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
        if not isinstance(other, Q6Contact):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
