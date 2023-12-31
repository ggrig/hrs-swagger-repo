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

class InsertPaymentPC(object):
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
        'insert_payment_pc': 'AllOfInsertPaymentPCInsertPaymentPc'
    }

    attribute_map = {
        'insert_payment_pc': 'InsertPaymentPC'
    }

    def __init__(self, insert_payment_pc=None):  # noqa: E501
        """InsertPaymentPC - a model defined in Swagger"""  # noqa: E501
        self._insert_payment_pc = None
        self.discriminator = None
        self.insert_payment_pc = insert_payment_pc

    @property
    def insert_payment_pc(self):
        """Gets the insert_payment_pc of this InsertPaymentPC.  # noqa: E501


        :return: The insert_payment_pc of this InsertPaymentPC.  # noqa: E501
        :rtype: AllOfInsertPaymentPCInsertPaymentPc
        """
        return self._insert_payment_pc

    @insert_payment_pc.setter
    def insert_payment_pc(self, insert_payment_pc):
        """Sets the insert_payment_pc of this InsertPaymentPC.


        :param insert_payment_pc: The insert_payment_pc of this InsertPaymentPC.  # noqa: E501
        :type: AllOfInsertPaymentPCInsertPaymentPc
        """
        if insert_payment_pc is None:
            raise ValueError("Invalid value for `insert_payment_pc`, must not be `None`")  # noqa: E501

        self._insert_payment_pc = insert_payment_pc

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
        if issubclass(InsertPaymentPC, dict):
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
        if not isinstance(other, InsertPaymentPC):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
