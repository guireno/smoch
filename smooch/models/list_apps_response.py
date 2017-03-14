# coding: utf-8

"""
    Smooch

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class ListAppsResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, apps=None, has_more=None, name=None):
        """
        ListAppsResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'apps': 'list[App]',
            'has_more': 'bool',
            'name': 'str'
        }

        self.attribute_map = {
            'apps': 'apps',
            'has_more': 'hasMore',
            'name': 'name'
        }

        self._apps = apps
        self._has_more = has_more
        self._name = name

    @property
    def apps(self):
        """
        Gets the apps of this ListAppsResponse.

        :return: The apps of this ListAppsResponse.
        :rtype: list[App]
        """
        return self._apps

    @apps.setter
    def apps(self, apps):
        """
        Sets the apps of this ListAppsResponse.

        :param apps: The apps of this ListAppsResponse.
        :type: list[App]
        """

        self._apps = apps

    @property
    def has_more(self):
        """
        Gets the has_more of this ListAppsResponse.

        :return: The has_more of this ListAppsResponse.
        :rtype: bool
        """
        return self._has_more

    @has_more.setter
    def has_more(self, has_more):
        """
        Sets the has_more of this ListAppsResponse.

        :param has_more: The has_more of this ListAppsResponse.
        :type: bool
        """

        self._has_more = has_more

    @property
    def name(self):
        """
        Gets the name of this ListAppsResponse.

        :return: The name of this ListAppsResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ListAppsResponse.

        :param name: The name of this ListAppsResponse.
        :type: str
        """

        self._name = name

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, ListAppsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other