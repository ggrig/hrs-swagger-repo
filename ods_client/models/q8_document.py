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

class Q8Document(object):
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
        'document_no': 'str'
    }

    attribute_map = {
        'document_no': 'DocumentNo'
    }

    def __init__(self, document_no=None):  # noqa: E501
        """Q8Document - a model defined in Swagger"""  # noqa: E501
        self._document_no = None
        self.discriminator = None
        self.document_no = document_no

    @property
    def document_no(self):
        """Gets the document_no of this Q8Document.  # noqa: E501


        :return: The document_no of this Q8Document.  # noqa: E501
        :rtype: str
        """
        return self._document_no

    @document_no.setter
    def document_no(self, document_no):
        """Sets the document_no of this Q8Document.


        :param document_no: The document_no of this Q8Document.  # noqa: E501
        :type: str
        """
        if document_no is None:
            raise ValueError("Invalid value for `document_no`, must not be `None`")  # noqa: E501

        self._document_no = document_no

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
        if issubclass(Q8Document, dict):
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
        if not isinstance(other, Q8Document):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other