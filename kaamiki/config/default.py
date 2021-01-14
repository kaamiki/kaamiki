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

"""Kaamiki's default configurations."""

from typing import Any

from kaamiki.config import constants

__all__ = ['SettingsConfigurator']


class SettingsConfigurator(object):
    """
    Base class for providing default configuration settings.

    The class uses ``__init_subclass__`` to fire up the moment any
    class inherits from it. This enables the pre-loading of the default
    settings.
    """

    _attrs = [setting for setting in dir(constants) if setting.isupper()]
    _read_only_attrs = [attr[2:] for attr in _attrs if attr.startswith('__')]

    @classmethod
    def __init_subclass__(cls) -> None:
        """Initialize subclass with default configuration settings."""
        # This pre-loading and initialization ensures that the default
        # settings are set before they are overridden by the user.
        for setting in cls._attrs:
            attr = setting[2:] if setting.startswith('__') else setting
            setattr(cls, attr, getattr(constants, setting))

    def __setattr__(self, attr: str, value: Any) -> None:
        """Raise exception when overridding read-only attributes."""
        if attr in self.__class__._read_only_attrs:
            raise ValueError(f'Cannot set {attr!r} attribute')
        return super().__setattr__(attr, value)
