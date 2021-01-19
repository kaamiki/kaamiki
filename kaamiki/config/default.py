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

import re
from typing import Any

from kaamiki.config import constants

__all__ = ['DefaultSettingsConfigurator']

_read_only_re = re.compile(r'^(\_[^_])')
_attrs = [attr for attr in dir(constants) if attr.isupper()]
_read_only_attrs = [attr[1:] for attr in _attrs if _read_only_re.match(attr)]


class DefaultSettingsConfigurator(object):
    """
    Base class for providing default configuration settings.

    The class uses ``__init_subclass__`` to fire up the moment any
    class inherits from it. This enables the pre-loading of the default
    settings.
    """

    @classmethod
    def __init_subclass__(cls) -> None:
        """Initialize subclass with default configuration settings."""
        # This pre-loading and initialization ensures that the default
        # settings are set before they are overridden by the user.
        for _attr in _attrs:
            if not _attr.startswith('__'):
                attr = _attr[1:] if _read_only_re.match(_attr) else _attr
                setattr(cls, attr, getattr(constants, _attr))

    def __setattr__(self, attr: str, value: Any) -> None:
        """Raise exception when overridding read-only attributes."""
        if attr in _read_only_attrs:
            raise ValueError(f'Cannot set {attr!r} attribute')
        return super().__setattr__(attr, value)
