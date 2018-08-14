# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from pfeffernusse.models.base_model_ import Model
from pfeffernusse import util


class XYZ(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, x: float=None, y: float=None, z: float=None, unit: str=None):  # noqa: E501
        """XYZ - a model defined in OpenAPI

        :param x: The x of this XYZ.  # noqa: E501
        :type x: float
        :param y: The y of this XYZ.  # noqa: E501
        :type y: float
        :param z: The z of this XYZ.  # noqa: E501
        :type z: float
        :param unit: The unit of this XYZ.  # noqa: E501
        :type unit: str
        """
        self.openapi_types = {
            'x': float,
            'y': float,
            'z': float,
            'unit': str
        }

        self.attribute_map = {
            'x': 'x',
            'y': 'y',
            'z': 'z',
            'unit': 'unit'
        }

        self._x = x
        self._y = y
        self._z = z
        self._unit = unit

    @classmethod
    def from_dict(cls, dikt) -> 'XYZ':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The XYZ of this XYZ.  # noqa: E501
        :rtype: XYZ
        """
        return util.deserialize_model(dikt, cls)

    @property
    def x(self) -> float:
        """Gets the x of this XYZ.


        :return: The x of this XYZ.
        :rtype: float
        """
        return self._x

    @x.setter
    def x(self, x: float):
        """Sets the x of this XYZ.


        :param x: The x of this XYZ.
        :type x: float
        """
        if x is None:
            raise ValueError("Invalid value for `x`, must not be `None`")  # noqa: E501

        self._x = x

    @property
    def y(self) -> float:
        """Gets the y of this XYZ.


        :return: The y of this XYZ.
        :rtype: float
        """
        return self._y

    @y.setter
    def y(self, y: float):
        """Sets the y of this XYZ.


        :param y: The y of this XYZ.
        :type y: float
        """
        if y is None:
            raise ValueError("Invalid value for `y`, must not be `None`")  # noqa: E501

        self._y = y

    @property
    def z(self) -> float:
        """Gets the z of this XYZ.


        :return: The z of this XYZ.
        :rtype: float
        """
        return self._z

    @z.setter
    def z(self, z: float):
        """Sets the z of this XYZ.


        :param z: The z of this XYZ.
        :type z: float
        """
        if z is None:
            raise ValueError("Invalid value for `z`, must not be `None`")  # noqa: E501

        self._z = z

    @property
    def unit(self) -> str:
        """Gets the unit of this XYZ.


        :return: The unit of this XYZ.
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit: str):
        """Sets the unit of this XYZ.


        :param unit: The unit of this XYZ.
        :type unit: str
        """
        if unit is None:
            raise ValueError("Invalid value for `unit`, must not be `None`")  # noqa: E501

        self._unit = unit
