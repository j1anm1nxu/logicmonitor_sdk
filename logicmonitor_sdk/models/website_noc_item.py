# coding: utf-8

"""
    LogicMonitor REST API

    LogicMonitor is a SaaS-based performance monitoring platform that provides full visibility into complex, hybrid infrastructures, offering granular performance monitoring and actionable data and insights. logicmonitor_sdk enables you to manage your LogicMonitor account programmatically.  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from logicmonitor_sdk.models.noc_item_base import NOCItemBase  # noqa: F401,E501


class WebsiteNOCItem(NOCItemBase):
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
        'type': 'str',
        'website_name': 'str',
        'name': 'str',
        'website_group_name': 'str',
        'group_by': 'str'
    }

    attribute_map = {
        'type': 'type',
        'website_name': 'websiteName',
        'name': 'name',
        'website_group_name': 'websiteGroupName',
        'group_by': 'groupBy'
    }

    def __init__(self, type=None, website_name=None, name=None, website_group_name=None, group_by=None):  # noqa: E501
        """WebsiteNOCItem - a model defined in Swagger"""  # noqa: E501

        self._type = None
        self._website_name = None
        self._name = None
        self._website_group_name = None
        self._group_by = None
        self.discriminator = None

        self.type = type
        self.website_name = website_name
        self.name = name
        self.website_group_name = website_group_name
        if group_by is not None:
            self.group_by = group_by

    @property
    def type(self):
        """Gets the type of this WebsiteNOCItem.  # noqa: E501


        :return: The type of this WebsiteNOCItem.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this WebsiteNOCItem.


        :param type: The type of this WebsiteNOCItem.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def website_name(self):
        """Gets the website_name of this WebsiteNOCItem.  # noqa: E501


        :return: The website_name of this WebsiteNOCItem.  # noqa: E501
        :rtype: str
        """
        return self._website_name

    @website_name.setter
    def website_name(self, website_name):
        """Sets the website_name of this WebsiteNOCItem.


        :param website_name: The website_name of this WebsiteNOCItem.  # noqa: E501
        :type: str
        """
        if website_name is None:
            raise ValueError("Invalid value for `website_name`, must not be `None`")  # noqa: E501

        self._website_name = website_name

    @property
    def name(self):
        """Gets the name of this WebsiteNOCItem.  # noqa: E501


        :return: The name of this WebsiteNOCItem.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this WebsiteNOCItem.


        :param name: The name of this WebsiteNOCItem.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def website_group_name(self):
        """Gets the website_group_name of this WebsiteNOCItem.  # noqa: E501


        :return: The website_group_name of this WebsiteNOCItem.  # noqa: E501
        :rtype: str
        """
        return self._website_group_name

    @website_group_name.setter
    def website_group_name(self, website_group_name):
        """Sets the website_group_name of this WebsiteNOCItem.


        :param website_group_name: The website_group_name of this WebsiteNOCItem.  # noqa: E501
        :type: str
        """
        if website_group_name is None:
            raise ValueError("Invalid value for `website_group_name`, must not be `None`")  # noqa: E501

        self._website_group_name = website_group_name

    @property
    def group_by(self):
        """Gets the group_by of this WebsiteNOCItem.  # noqa: E501


        :return: The group_by of this WebsiteNOCItem.  # noqa: E501
        :rtype: str
        """
        return self._group_by

    @group_by.setter
    def group_by(self, group_by):
        """Sets the group_by of this WebsiteNOCItem.


        :param group_by: The group_by of this WebsiteNOCItem.  # noqa: E501
        :type: str
        """

        self._group_by = group_by

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
        if issubclass(WebsiteNOCItem, dict):
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
        if not isinstance(other, WebsiteNOCItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
