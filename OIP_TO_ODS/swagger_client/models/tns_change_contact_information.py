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

class TnsChangeContactInformation(object):
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
        'contact_information': 'AllOftnsChangeContactInformationContactInformation'
    }

    attribute_map = {
        'contact_information': 'contactInformation'
    }

    def __init__(self, contact_information=None):  # noqa: E501
        """TnsChangeContactInformation - a model defined in Swagger"""  # noqa: E501
        self._contact_information = None
        self.discriminator = None
        self.contact_information = contact_information

    @property
    def contact_information(self):
        """Gets the contact_information of this TnsChangeContactInformation.  # noqa: E501


        :return: The contact_information of this TnsChangeContactInformation.  # noqa: E501
        :rtype: AllOftnsChangeContactInformationContactInformation
        """
        return self._contact_information

    @contact_information.setter
    def contact_information(self, contact_information):
        """Sets the contact_information of this TnsChangeContactInformation.


        :param contact_information: The contact_information of this TnsChangeContactInformation.  # noqa: E501
        :type: AllOftnsChangeContactInformationContactInformation
        """
        if contact_information is None:
            raise ValueError("Invalid value for `contact_information`, must not be `None`")  # noqa: E501

        self._contact_information = contact_information

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
        if issubclass(TnsChangeContactInformation, dict):
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
        if not isinstance(other, TnsChangeContactInformation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
