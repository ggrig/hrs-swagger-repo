# coding: utf-8

"""
    OIP API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class BookingsourceBody(object):
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
        'no': 'str',
        'category': 'str',
        'name': 'str',
        'tenant': 'str'
    }

    attribute_map = {
        'no': 'No',
        'category': 'Category',
        'name': 'Name',
        'tenant': 'Tenant'
    }

    def __init__(self, no=None, category=None, name=None, tenant=None):  # noqa: E501
        """BookingsourceBody - a model defined in Swagger"""  # noqa: E501
        self._no = None
        self._category = None
        self._name = None
        self._tenant = None
        self.discriminator = None
        if no is not None:
            self.no = no
        if category is not None:
            self.category = category
        if name is not None:
            self.name = name
        if tenant is not None:
            self.tenant = tenant

    @property
    def no(self):
        """Gets the no of this BookingsourceBody.  # noqa: E501

        The booking source number  # noqa: E501

        :return: The no of this BookingsourceBody.  # noqa: E501
        :rtype: str
        """
        return self._no

    @no.setter
    def no(self, no):
        """Sets the no of this BookingsourceBody.

        The booking source number  # noqa: E501

        :param no: The no of this BookingsourceBody.  # noqa: E501
        :type: str
        """

        self._no = no

    @property
    def category(self):
        """Gets the category of this BookingsourceBody.  # noqa: E501

        The category of the booking source  # noqa: E501

        :return: The category of this BookingsourceBody.  # noqa: E501
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this BookingsourceBody.

        The category of the booking source  # noqa: E501

        :param category: The category of this BookingsourceBody.  # noqa: E501
        :type: str
        """

        self._category = category

    @property
    def name(self):
        """Gets the name of this BookingsourceBody.  # noqa: E501

        The name of the booking source  # noqa: E501

        :return: The name of this BookingsourceBody.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BookingsourceBody.

        The name of the booking source  # noqa: E501

        :param name: The name of this BookingsourceBody.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def tenant(self):
        """Gets the tenant of this BookingsourceBody.  # noqa: E501

        The tenant name  # noqa: E501

        :return: The tenant of this BookingsourceBody.  # noqa: E501
        :rtype: str
        """
        return self._tenant

    @tenant.setter
    def tenant(self, tenant):
        """Sets the tenant of this BookingsourceBody.

        The tenant name  # noqa: E501

        :param tenant: The tenant of this BookingsourceBody.  # noqa: E501
        :type: str
        """

        self._tenant = tenant

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
        if issubclass(BookingsourceBody, dict):
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
        if not isinstance(other, BookingsourceBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other