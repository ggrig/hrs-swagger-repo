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

class ConfirmInvoiceResult(object):
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
        'confirm_invoice_result': 'AllOfConfirmInvoiceResultConfirmInvoiceResult'
    }

    attribute_map = {
        'confirm_invoice_result': 'ConfirmInvoice_Result'
    }

    def __init__(self, confirm_invoice_result=None):  # noqa: E501
        """ConfirmInvoiceResult - a model defined in Swagger"""  # noqa: E501
        self._confirm_invoice_result = None
        self.discriminator = None
        self.confirm_invoice_result = confirm_invoice_result

    @property
    def confirm_invoice_result(self):
        """Gets the confirm_invoice_result of this ConfirmInvoiceResult.  # noqa: E501


        :return: The confirm_invoice_result of this ConfirmInvoiceResult.  # noqa: E501
        :rtype: AllOfConfirmInvoiceResultConfirmInvoiceResult
        """
        return self._confirm_invoice_result

    @confirm_invoice_result.setter
    def confirm_invoice_result(self, confirm_invoice_result):
        """Sets the confirm_invoice_result of this ConfirmInvoiceResult.


        :param confirm_invoice_result: The confirm_invoice_result of this ConfirmInvoiceResult.  # noqa: E501
        :type: AllOfConfirmInvoiceResultConfirmInvoiceResult
        """
        if confirm_invoice_result is None:
            raise ValueError("Invalid value for `confirm_invoice_result`, must not be `None`")  # noqa: E501

        self._confirm_invoice_result = confirm_invoice_result

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
        if issubclass(ConfirmInvoiceResult, dict):
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
        if not isinstance(other, ConfirmInvoiceResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
