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

class ChangeContactInformation(object):
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
        'change_contact_information': 'AllOfChangeContactInformationChangeContactInformation'
    }

    attribute_map = {
        'change_contact_information': 'ChangeContactInformation'
    }

    def __init__(self, change_contact_information=None):  # noqa: E501
        """ChangeContactInformation - a model defined in Swagger"""  # noqa: E501
        self._change_contact_information = None
        self.discriminator = None
        self.change_contact_information = change_contact_information

    @property
    def change_contact_information(self):
        """Gets the change_contact_information of this ChangeContactInformation.  # noqa: E501


        :return: The change_contact_information of this ChangeContactInformation.  # noqa: E501
        :rtype: AllOfChangeContactInformationChangeContactInformation
        """
        return self._change_contact_information

    @change_contact_information.setter
    def change_contact_information(self, change_contact_information):
        """Sets the change_contact_information of this ChangeContactInformation.


        :param change_contact_information: The change_contact_information of this ChangeContactInformation.  # noqa: E501
        :type: AllOfChangeContactInformationChangeContactInformation
        """
        if change_contact_information is None:
            raise ValueError("Invalid value for `change_contact_information`, must not be `None`")  # noqa: E501

        self._change_contact_information = change_contact_information

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
        if issubclass(ChangeContactInformation, dict):
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
        if not isinstance(other, ChangeContactInformation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
