# Copyright (c) 2021 Kaamiki Development Team. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Author(s):
#           xames3 <xames3.kaamiki@gmail.com>

"""
Module for declaring constraints on the object based on their type.
"""

from abc import ABC, abstractclassmethod
from collections.abc import Iterable
from typing import Any, Callable, List

from kaamiki.utils.exceptions import KaamikiError, UnexpectedTypeError

__all__ = ['Type', 'String']


def _join(iterable: List, and_or: str) -> str:
    """Join iterables grammatically."""
    return ', '.join(iterable[:-2] + [f' {and_or} '.join(iterable[-2:])])


def _assert(cond: bool, exc: Callable = KaamikiError, **kwargs: Any) -> None:
    """Emulate assertion behaviour."""
    if not cond:
        raise exc(valid=True, **kwargs)


class Contract(ABC):
    """
    Contract class for declaring constraints on the input data. If the
    conditions aren't met, exceptions are raised.
    """

    @abstractclassmethod
    def check(cls, value: Any) -> None:
        pass


class Type(Contract):
    """
    An extension to the Contract class to check the type of an object.

    Usage::

            class SomeDataStructureToValidate(Type):
                _type = (valid python object)

    Example::

        >>> class String(Type):
        ...     _type = str
        ...
        >>> String.check('XA is God')
        >>> String.check(69.0)
        Traceback (most recent call last):
        ...
        UnexpectedTypeError: Expected str, got float instead

        >>> class Number(Type):
        ...     _type = (int, float)
        ...
        >>> Number.check(69)
        >>> Number.check(69.0)
        >>> Number.check(69)
        Traceback (most recent call last):
        ...
        UnexpectedTypeError: Expected either int or float, got str instead
    """

    _type = object

    @classmethod
    def check(cls, value: Any) -> None:
        got = type(value).__name__
        if cls._type is None:
            msg = f'Expected NoneType, got {got} instead'
            cls._type = type(None)
        elif not isinstance(cls._type, Iterable):
            msg = f'Expected {cls._type.__name__}, got {got} instead'
        else:
            # pyright: reportGeneralTypeIssues=false
            types = [_type.__name__ for _type in cls._type]
            msg = f'Expected either {_join(types, "or")}, got {got} instead'
        _assert(isinstance(value, cls._type), UnexpectedTypeError, msg=msg)
        super().check(value)


class String(Type):
    """Class to check if the object is a string."""
    _type = str
