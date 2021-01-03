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

"""Module for validating objects based on their type."""

from abc import ABC, abstractclassmethod
from typing import Any


class Contract(ABC):
    """
    Contract class for declaring constraints on the input data. If the
    conditions aren't met, exceptions are raised.
    """

    @abstractclassmethod
    def check(cls, value: Any) -> None:
        pass
