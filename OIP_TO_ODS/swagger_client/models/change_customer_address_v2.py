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

class ChangeCustomerAddressV2(object):
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
        'change_customer_address_v2': 'AllOfChangeCustomerAddressV2ChangeCustomerAddressV2'
    }

    attribute_map = {
        'change_customer_address_v2': 'ChangeCustomerAddressV2'
    }

    def __init__(self, change_customer_address_v2=None):  # noqa: E501
        """ChangeCustomerAddressV2 - a model defined in Swagger"""  # noqa: E501
        self._change_customer_address_v2 = None
        self.discriminator = None
        self.change_customer_address_v2 = change_customer_address_v2

    @property
    def change_customer_address_v2(self):
        """Gets the change_customer_address_v2 of this ChangeCustomerAddressV2.  # noqa: E501


        :return: The change_customer_address_v2 of this ChangeCustomerAddressV2.  # noqa: E501
        :rtype: AllOfChangeCustomerAddressV2ChangeCustomerAddressV2
        """
        return self._change_customer_address_v2

    @change_customer_address_v2.setter
    def change_customer_address_v2(self, change_customer_address_v2):
        """Sets the change_customer_address_v2 of this ChangeCustomerAddressV2.


        :param change_customer_address_v2: The change_customer_address_v2 of this ChangeCustomerAddressV2.  # noqa: E501
        :type: AllOfChangeCustomerAddressV2ChangeCustomerAddressV2
        """
        if change_customer_address_v2 is None:
            raise ValueError("Invalid value for `change_customer_address_v2`, must not be `None`")  # noqa: E501

        self._change_customer_address_v2 = change_customer_address_v2

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
        if issubclass(ChangeCustomerAddressV2, dict):
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
        if not isinstance(other, ChangeCustomerAddressV2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
