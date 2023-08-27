# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class WithdrawValueDTO(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, value=None):  # noqa: E501
        """WithdrawValueDTO - a model defined in OpenAPI

        :param value: The value of this WithdrawValueDTO.  # noqa: E501
        :type value: int
        """
        self.openapi_types = {
            'value': int
        }

        self.attribute_map = {
            'value': 'value'
        }

        self._value = value

    @classmethod
    def from_dict(cls, dikt) -> 'WithdrawValueDTO':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The withdraw_value_dto of this WithdrawValueDTO.  # noqa: E501
        :rtype: WithdrawValueDTO
        """
        return util.deserialize_model(dikt, cls)

    @property
    def value(self):
        """Gets the value of this WithdrawValueDTO.


        :return: The value of this WithdrawValueDTO.
        :rtype: int
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this WithdrawValueDTO.


        :param value: The value of this WithdrawValueDTO.
        :type value: int
        """

        self._value = value