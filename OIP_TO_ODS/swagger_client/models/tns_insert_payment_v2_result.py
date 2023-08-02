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

class TnsInsertPaymentV2Result(object):
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
        'insert_payment': 'AllOftnsInsertPaymentV2ResultInsertPayment'
    }

    attribute_map = {
        'insert_payment': 'insertPayment'
    }

    def __init__(self, insert_payment=None):  # noqa: E501
        """TnsInsertPaymentV2Result - a model defined in Swagger"""  # noqa: E501
        self._insert_payment = None
        self.discriminator = None
        self.insert_payment = insert_payment

    @property
    def insert_payment(self):
        """Gets the insert_payment of this TnsInsertPaymentV2Result.  # noqa: E501


        :return: The insert_payment of this TnsInsertPaymentV2Result.  # noqa: E501
        :rtype: AllOftnsInsertPaymentV2ResultInsertPayment
        """
        return self._insert_payment

    @insert_payment.setter
    def insert_payment(self, insert_payment):
        """Sets the insert_payment of this TnsInsertPaymentV2Result.


        :param insert_payment: The insert_payment of this TnsInsertPaymentV2Result.  # noqa: E501
        :type: AllOftnsInsertPaymentV2ResultInsertPayment
        """
        if insert_payment is None:
            raise ValueError("Invalid value for `insert_payment`, must not be `None`")  # noqa: E501

        self._insert_payment = insert_payment

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
        if issubclass(TnsInsertPaymentV2Result, dict):
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
        if not isinstance(other, TnsInsertPaymentV2Result):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
