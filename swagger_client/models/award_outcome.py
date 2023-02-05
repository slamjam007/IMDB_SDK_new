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

class AwardOutcome(object):
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
        'outcome_title': 'str',
        'outcome_category': 'str',
        'outcome_details': 'list[AwardOutcomeDetail]'
    }

    attribute_map = {
        'outcome_title': 'outcomeTitle',
        'outcome_category': 'outcomeCategory',
        'outcome_details': 'outcomeDetails'
    }

    def __init__(self, outcome_title=None, outcome_category=None, outcome_details=None):  # noqa: E501
        """AwardOutcome - a model defined in Swagger"""  # noqa: E501
        self._outcome_title = None
        self._outcome_category = None
        self._outcome_details = None
        self.discriminator = None
        if outcome_title is not None:
            self.outcome_title = outcome_title
        if outcome_category is not None:
            self.outcome_category = outcome_category
        if outcome_details is not None:
            self.outcome_details = outcome_details

    @property
    def outcome_title(self):
        """Gets the outcome_title of this AwardOutcome.  # noqa: E501


        :return: The outcome_title of this AwardOutcome.  # noqa: E501
        :rtype: str
        """
        return self._outcome_title

    @outcome_title.setter
    def outcome_title(self, outcome_title):
        """Sets the outcome_title of this AwardOutcome.


        :param outcome_title: The outcome_title of this AwardOutcome.  # noqa: E501
        :type: str
        """

        self._outcome_title = outcome_title

    @property
    def outcome_category(self):
        """Gets the outcome_category of this AwardOutcome.  # noqa: E501


        :return: The outcome_category of this AwardOutcome.  # noqa: E501
        :rtype: str
        """
        return self._outcome_category

    @outcome_category.setter
    def outcome_category(self, outcome_category):
        """Sets the outcome_category of this AwardOutcome.


        :param outcome_category: The outcome_category of this AwardOutcome.  # noqa: E501
        :type: str
        """

        self._outcome_category = outcome_category

    @property
    def outcome_details(self):
        """Gets the outcome_details of this AwardOutcome.  # noqa: E501


        :return: The outcome_details of this AwardOutcome.  # noqa: E501
        :rtype: list[AwardOutcomeDetail]
        """
        return self._outcome_details

    @outcome_details.setter
    def outcome_details(self, outcome_details):
        """Sets the outcome_details of this AwardOutcome.


        :param outcome_details: The outcome_details of this AwardOutcome.  # noqa: E501
        :type: list[AwardOutcomeDetail]
        """

        self._outcome_details = outcome_details

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
        if issubclass(AwardOutcome, dict):
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
        if not isinstance(other, AwardOutcome):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other