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

class Q28HotelBankAccountInfoList(object):
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
        'hotel_bank_account_info': 'list[Q28HotelBankAccountInfo]'
    }

    attribute_map = {
        'hotel_bank_account_info': 'HotelBankAccountInfo'
    }

    def __init__(self, hotel_bank_account_info=None):  # noqa: E501
        """Q28HotelBankAccountInfoList - a model defined in Swagger"""  # noqa: E501
        self._hotel_bank_account_info = None
        self.discriminator = None
        self.hotel_bank_account_info = hotel_bank_account_info

    @property
    def hotel_bank_account_info(self):
        """Gets the hotel_bank_account_info of this Q28HotelBankAccountInfoList.  # noqa: E501


        :return: The hotel_bank_account_info of this Q28HotelBankAccountInfoList.  # noqa: E501
        :rtype: list[Q28HotelBankAccountInfo]
        """
        return self._hotel_bank_account_info

    @hotel_bank_account_info.setter
    def hotel_bank_account_info(self, hotel_bank_account_info):
        """Sets the hotel_bank_account_info of this Q28HotelBankAccountInfoList.


        :param hotel_bank_account_info: The hotel_bank_account_info of this Q28HotelBankAccountInfoList.  # noqa: E501
        :type: list[Q28HotelBankAccountInfo]
        """
        if hotel_bank_account_info is None:
            raise ValueError("Invalid value for `hotel_bank_account_info`, must not be `None`")  # noqa: E501

        self._hotel_bank_account_info = hotel_bank_account_info

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
        if issubclass(Q28HotelBankAccountInfoList, dict):
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
        if not isinstance(other, Q28HotelBankAccountInfoList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
