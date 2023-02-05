# coding: utf-8

"""
    IMDb-API

    The IMDb-API Documentation. You need a <a href='/Identity/Account/Manage' target='_blank'><code>API Key</code></a> for testing APIs.<br/><a class='link' href='/API'>Back to API Tester</a>  # noqa: E501

    OpenAPI spec version: 1.9.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class IMDbListData(object):
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
        'title': 'str',
        'by': 'str',
        'created': 'str',
        'updated': 'str',
        'description': 'str',
        'items': 'list[IMDbListDataDetail]',
        'error_message': 'str'
    }

    attribute_map = {
        'title': 'title',
        'by': 'by',
        'created': 'created',
        'updated': 'updated',
        'description': 'description',
        'items': 'items',
        'error_message': 'errorMessage'
    }

    def __init__(self, title=None, by=None, created=None, updated=None, description=None, items=None, error_message=None):  # noqa: E501
        """IMDbListData - a model defined in Swagger"""  # noqa: E501
        self._title = None
        self._by = None
        self._created = None
        self._updated = None
        self._description = None
        self._items = None
        self._error_message = None
        self.discriminator = None
        if title is not None:
            self.title = title
        if by is not None:
            self.by = by
        if created is not None:
            self.created = created
        if updated is not None:
            self.updated = updated
        if description is not None:
            self.description = description
        if items is not None:
            self.items = items
        if error_message is not None:
            self.error_message = error_message

    @property
    def title(self):
        """Gets the title of this IMDbListData.  # noqa: E501


        :return: The title of this IMDbListData.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this IMDbListData.


        :param title: The title of this IMDbListData.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def by(self):
        """Gets the by of this IMDbListData.  # noqa: E501


        :return: The by of this IMDbListData.  # noqa: E501
        :rtype: str
        """
        return self._by

    @by.setter
    def by(self, by):
        """Sets the by of this IMDbListData.


        :param by: The by of this IMDbListData.  # noqa: E501
        :type: str
        """

        self._by = by

    @property
    def created(self):
        """Gets the created of this IMDbListData.  # noqa: E501


        :return: The created of this IMDbListData.  # noqa: E501
        :rtype: str
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this IMDbListData.


        :param created: The created of this IMDbListData.  # noqa: E501
        :type: str
        """

        self._created = created

    @property
    def updated(self):
        """Gets the updated of this IMDbListData.  # noqa: E501


        :return: The updated of this IMDbListData.  # noqa: E501
        :rtype: str
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this IMDbListData.


        :param updated: The updated of this IMDbListData.  # noqa: E501
        :type: str
        """

        self._updated = updated

    @property
    def description(self):
        """Gets the description of this IMDbListData.  # noqa: E501


        :return: The description of this IMDbListData.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this IMDbListData.


        :param description: The description of this IMDbListData.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def items(self):
        """Gets the items of this IMDbListData.  # noqa: E501


        :return: The items of this IMDbListData.  # noqa: E501
        :rtype: list[IMDbListDataDetail]
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this IMDbListData.


        :param items: The items of this IMDbListData.  # noqa: E501
        :type: list[IMDbListDataDetail]
        """

        self._items = items

    @property
    def error_message(self):
        """Gets the error_message of this IMDbListData.  # noqa: E501


        :return: The error_message of this IMDbListData.  # noqa: E501
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        """Sets the error_message of this IMDbListData.


        :param error_message: The error_message of this IMDbListData.  # noqa: E501
        :type: str
        """

        self._error_message = error_message

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
        if issubclass(IMDbListData, dict):
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
        if not isinstance(other, IMDbListData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other