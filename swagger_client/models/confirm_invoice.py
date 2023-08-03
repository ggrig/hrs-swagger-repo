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

class ConfirmInvoice(object):
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
        'confirm_invoice': 'AllOfConfirmInvoiceConfirmInvoice'
    }

    attribute_map = {
        'confirm_invoice': 'ConfirmInvoice'
    }

    def __init__(self, confirm_invoice=None):  # noqa: E501
        """ConfirmInvoice - a model defined in Swagger"""  # noqa: E501
        self._confirm_invoice = None
        self.discriminator = None
        self.confirm_invoice = confirm_invoice

    @property
    def confirm_invoice(self):
        """Gets the confirm_invoice of this ConfirmInvoice.  # noqa: E501


        :return: The confirm_invoice of this ConfirmInvoice.  # noqa: E501
        :rtype: AllOfConfirmInvoiceConfirmInvoice
        """
        return self._confirm_invoice

    @confirm_invoice.setter
    def confirm_invoice(self, confirm_invoice):
        """Sets the confirm_invoice of this ConfirmInvoice.


        :param confirm_invoice: The confirm_invoice of this ConfirmInvoice.  # noqa: E501
        :type: AllOfConfirmInvoiceConfirmInvoice
        """
        # TBD:
        # if confirm_invoice is None:
        #     raise ValueError("Invalid value for `confirm_invoice`, must not be `None`")  # noqa: E501

        self._confirm_invoice = confirm_invoice

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
        if issubclass(ConfirmInvoice, dict):
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
        if not isinstance(other, ConfirmInvoice):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
