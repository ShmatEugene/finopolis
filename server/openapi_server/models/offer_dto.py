# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class OfferDTO(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id=None, cfa_image_id=None, count=None, price=None, seller=None):  # noqa: E501
        """OfferDTO - a model defined in OpenAPI

        :param id: The id of this OfferDTO.  # noqa: E501
        :type id: int
        :param cfa_image_id: The cfa_image_id of this OfferDTO.  # noqa: E501
        :type cfa_image_id: int
        :param count: The count of this OfferDTO.  # noqa: E501
        :type count: int
        :param price: The price of this OfferDTO.  # noqa: E501
        :type price: int
        :param seller: The seller of this OfferDTO.  # noqa: E501
        :type seller: int
        """
        self.openapi_types = {
            'id': int,
            'cfa_image_id': int,
            'count': int,
            'price': int,
            'seller': 'PublicUser'
        }

        self.attribute_map = {
            'id': 'id',
            'cfa_image_id': 'cfa_image_id',
            'count': 'count',
            'price': 'price',
            'seller': 'seller'
        }

        self._id = id
        self._cfa_image_id = cfa_image_id
        self._count = count
        self._price = price
        self._seller = seller

    @classmethod
    def from_dict(cls, dikt) -> 'OfferDTO':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The offer_dto of this OfferDTO.  # noqa: E501
        :rtype: OfferDTO
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self):
        """Gets the id of this OfferDTO.


        :return: The id of this OfferDTO.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this OfferDTO.


        :param id: The id of this OfferDTO.
        :type id: int
        """

        self._id = id

    @property
    def cfa_image_id(self):
        """Gets the cfa_image_id of this OfferDTO.


        :return: The cfa_image_id of this OfferDTO.
        :rtype: int
        """
        return self._cfa_image_id

    @cfa_image_id.setter
    def cfa_image_id(self, cfa_image_id):
        """Sets the cfa_image_id of this OfferDTO.


        :param cfa_image_id: The cfa_image_id of this OfferDTO.
        :type cfa_image_id: int
        """

        self._cfa_image_id = cfa_image_id

    @property
    def count(self):
        """Gets the count of this OfferDTO.


        :return: The count of this OfferDTO.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this OfferDTO.


        :param count: The count of this OfferDTO.
        :type count: int
        """

        self._count = count

    @property
    def price(self):
        """Gets the price of this OfferDTO.


        :return: The price of this OfferDTO.
        :rtype: int
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this OfferDTO.


        :param price: The price of this OfferDTO.
        :type price: int
        """

        self._price = price

    @property
    def seller(self):
        """Gets the seller of this OfferDTO.


        :return: The seller of this OfferDTO.
        :rtype: int
        """
        return self._seller

    @seller.setter
    def seller(self, seller):
        """Sets the seller of this OfferDTO.


        :param seller: The seller of this OfferDTO.
        :type seller: int
        """

        self._seller = seller
