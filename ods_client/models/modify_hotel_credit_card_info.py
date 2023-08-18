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

class ModifyHotelCreditCardInfo(object):
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
        'modify_hotel_credit_card_info': 'AllOfModifyHotelCreditCardInfoModifyHotelCreditCardInfo'
    }

    attribute_map = {
        'modify_hotel_credit_card_info': 'ModifyHotelCreditCardInfo'
    }

    def __init__(self, modify_hotel_credit_card_info=None):  # noqa: E501
        """ModifyHotelCreditCardInfo - a model defined in Swagger"""  # noqa: E501
        self._modify_hotel_credit_card_info = None
        self.discriminator = None
        self.modify_hotel_credit_card_info = modify_hotel_credit_card_info

    @property
    def modify_hotel_credit_card_info(self):
        """Gets the modify_hotel_credit_card_info of this ModifyHotelCreditCardInfo.  # noqa: E501


        :return: The modify_hotel_credit_card_info of this ModifyHotelCreditCardInfo.  # noqa: E501
        :rtype: AllOfModifyHotelCreditCardInfoModifyHotelCreditCardInfo
        """
        return self._modify_hotel_credit_card_info

    @modify_hotel_credit_card_info.setter
    def modify_hotel_credit_card_info(self, modify_hotel_credit_card_info):
        """Sets the modify_hotel_credit_card_info of this ModifyHotelCreditCardInfo.


        :param modify_hotel_credit_card_info: The modify_hotel_credit_card_info of this ModifyHotelCreditCardInfo.  # noqa: E501
        :type: AllOfModifyHotelCreditCardInfoModifyHotelCreditCardInfo
        """
        if modify_hotel_credit_card_info is None:
            raise ValueError("Invalid value for `modify_hotel_credit_card_info`, must not be `None`")  # noqa: E501

        self._modify_hotel_credit_card_info = modify_hotel_credit_card_info

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
        if issubclass(ModifyHotelCreditCardInfo, dict):
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
        if not isinstance(other, ModifyHotelCreditCardInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
