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
from swagger_client.models.q16_invoice_list import Q16InvoiceList  # noqa: F401,E501

class AllOftnsModifyInvoiceV2ModifyInvoice(Q16InvoiceList):
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
    }
    if hasattr(Q16InvoiceList, "swagger_types"):
        swagger_types.update(Q16InvoiceList.swagger_types)

    attribute_map = {
    }
    if hasattr(Q16InvoiceList, "attribute_map"):
        attribute_map.update(Q16InvoiceList.attribute_map)

    def __init__(self, *args, **kwargs):  # noqa: E501
        """AllOftnsModifyInvoiceV2ModifyInvoice - a model defined in Swagger"""  # noqa: E501
        self.discriminator = None
        Q16InvoiceList.__init__(self, *args, **kwargs)

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
        if issubclass(AllOftnsModifyInvoiceV2ModifyInvoice, dict):
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
        if not isinstance(other, AllOftnsModifyInvoiceV2ModifyInvoice):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
