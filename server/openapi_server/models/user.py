# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class User(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id=None, login=None, username=None, name=None, balance=None):  # noqa: E501
        """User - a model defined in OpenAPI

        :param id: The id of this User.  # noqa: E501
        :type id: int
        :param login: The login of this User.  # noqa: E501
        :type login: str
        :param username: The username of this User.  # noqa: E501
        :type username: str
        :param name: The name of this User.  # noqa: E501
        :type name: str
        :param balance: The balance of this User.  # noqa: E501
        :type balance: int
        """
        self.openapi_types = {
            'id': int,
            'login': str,
            'username': str,
            'name': str,
            'balance': int
        }

        self.attribute_map = {
            'id': 'id',
            'login': 'login',
            'username': 'username',
            'name': 'name',
            'balance': 'balance'
        }

        self._id = id
        self._login = login
        self._username = username
        self._name = name
        self._balance = balance

    @classmethod
    def from_dict(cls, dikt) -> 'User':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The User of this User.  # noqa: E501
        :rtype: User
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self):
        """Gets the id of this User.


        :return: The id of this User.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this User.


        :param id: The id of this User.
        :type id: int
        """

        self._id = id

    @property
    def login(self):
        """Gets the login of this User.


        :return: The login of this User.
        :rtype: str
        """
        return self._login

    @login.setter
    def login(self, login):
        """Sets the login of this User.


        :param login: The login of this User.
        :type login: str
        """

        self._login = login

    @property
    def username(self):
        """Gets the username of this User.


        :return: The username of this User.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this User.


        :param username: The username of this User.
        :type username: str
        """

        self._username = username

    @property
    def name(self):
        """Gets the name of this User.


        :return: The name of this User.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this User.


        :param name: The name of this User.
        :type name: str
        """

        self._name = name

    @property
    def balance(self):
        """Gets the balance of this User.


        :return: The balance of this User.
        :rtype: int
        """
        return self._balance

    @balance.setter
    def balance(self, balance):
        """Sets the balance of this User.


        :param balance: The balance of this User.
        :type balance: int
        """

        self._balance = balance
