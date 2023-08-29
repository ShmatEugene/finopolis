# coding: utf-8

from __future__ import absolute_import

from datetime import date, datetime  # noqa: F401
from typing import List, Dict  # noqa: F401

from openapi_server import util
from openapi_server.models.base_model_ import Model


class TradeDTO(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id=None, date=None, cfa_token=None, price=None, buyer=None, seller=None):  # noqa: E501
        """TradeDTO - a model defined in OpenAPI

        :param id: The id of this TradeDTO.  # noqa: E501
        :type id: int
        :param date: The date of this TradeDTO.  # noqa: E501
        :type date: datetime
        :param cfa_token: The cfa_token of this TradeDTO.  # noqa: E501
        :type cfa_token: str
        :param price: The price of this TradeDTO.  # noqa: E501
        :type price: float
        :param buyer: The buyer of this TradeDTO.  # noqa: E501
        :type buyer: int
        :param seller: The seller of this TradeDTO.  # noqa: E501
        :type seller: int
        """
        self.openapi_types = {
            'id': int,
            'date': datetime,
            'cfa_token': str,
            'price': float,
            'buyer': 'PublicUser',
            'seller': 'PublicUser'
        }

        self.attribute_map = {
            'id': 'id',
            'date': 'date',
            'cfa_token': 'cfa_token',
            'price': 'price',
            'buyer': 'buyer',
            'seller': 'seller'
        }

        self._id = id
        self._date = date
        self._cfa_token = cfa_token
        self._price = price
        self._buyer = buyer
        self._seller = seller

    @classmethod
    def from_dict(cls, dikt) -> 'TradeDTO':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The trade_dto of this TradeDTO.  # noqa: E501
        :rtype: TradeDTO
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self):
        """Gets the id of this TradeDTO.


        :return: The id of this TradeDTO.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TradeDTO.


        :param id: The id of this TradeDTO.
        :type id: int
        """

        self._id = id

    @property
    def date(self):
        """Gets the date of this TradeDTO.


        :return: The date of this TradeDTO.
        :rtype: str
        """
        return self._date

    @date.setter
    def date(self, date):
        """Sets the date of this TradeDTO.


        :param date: The date of this TradeDTO.
        :type date: str
        """

        self._date = date

    @property
    def cfa_token(self):
        """Gets the cfa_token of this TradeDTO.


        :return: The cfa_token of this TradeDTO.
        :rtype: str
        """
        return self._cfa_token

    @cfa_token.setter
    def cfa_token(self, cfa_token):
        """Sets the cfa_token of this TradeDTO.


        :param cfa_token: The cfa_token of this TradeDTO.
        :type cfa_token: str
        """

        self._cfa_token = cfa_token

    @property
    def price(self):
        """Gets the price of this TradeDTO.


        :return: The price of this TradeDTO.
        :rtype: int
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this TradeDTO.


        :param price: The price of this TradeDTO.
        :type price: int
        """

        self._price = price

    @property
    def buyer(self):
        """Gets the buyer of this TradeDTO.


        :return: The buyer of this TradeDTO.
        :rtype: int
        """
        return self._buyer

    @buyer.setter
    def buyer(self, buyer):
        """Sets the buyer of this TradeDTO.


        :param buyer: The buyer of this TradeDTO.
        :type buyer: int
        """

        self._buyer = buyer

    @property
    def seller(self):
        """Gets the seller of this TradeDTO.


        :return: The seller of this TradeDTO.
        :rtype: int
        """
        return self._seller

    @seller.setter
    def seller(self, seller):
        """Sets the seller of this TradeDTO.


        :param seller: The seller of this TradeDTO.
        :type seller: int
        """

        self._seller = seller
