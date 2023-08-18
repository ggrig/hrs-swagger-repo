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

class ModifyInvoice(object):
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
        'modify_invoice': 'AllOfModifyInvoiceModifyInvoice'
    }

    attribute_map = {
        'modify_invoice': 'ModifyInvoice'
    }

    def __init__(self, modify_invoice=None):  # noqa: E501
        """ModifyInvoice - a model defined in Swagger"""  # noqa: E501
        self._modify_invoice = None
        self.discriminator = None
        self.modify_invoice = modify_invoice

    @property
    def modify_invoice(self):
        """Gets the modify_invoice of this ModifyInvoice.  # noqa: E501


        :return: The modify_invoice of this ModifyInvoice.  # noqa: E501
        :rtype: AllOfModifyInvoiceModifyInvoice
        """
        return self._modify_invoice

    @modify_invoice.setter
    def modify_invoice(self, modify_invoice):
        """Sets the modify_invoice of this ModifyInvoice.


        :param modify_invoice: The modify_invoice of this ModifyInvoice.  # noqa: E501
        :type: AllOfModifyInvoiceModifyInvoice
        """
        if modify_invoice is None:
            raise ValueError("Invalid value for `modify_invoice`, must not be `None`")  # noqa: E501

        self._modify_invoice = modify_invoice

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
        if issubclass(ModifyInvoice, dict):
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
        if not isinstance(other, ModifyInvoice):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
