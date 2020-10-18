# Copyright (c) 2020 Kaamiki Development Team. All rights reserved.
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
#     xames3 <44119552+xames3@users.noreply.github.com>

"""
Kaamiki

A Python implementation of Kaamiki.
"""

import getpass
import threading

USER = getpass.getuser().replace(" ", "-").lower()


class Neo(type):
  """
  A thread-safe implementation of Singleton design pattern.

  Singleton is a creational design pattern, which ensures that
  only a single object of its kind exist and provides a single
  point of access to it for any other code.
  The below is a thread-safe implementation of the Singleton
  design pattern. You can instantiate a class multiple times
  and yet you would get reference to the same object.

  See https://stackoverflow.com/q/6760685 for more methods of
  implementing singletons in code.

  Example:
    >>> class YourClass(metaclass=Neo):
    ...     pass
    ...
    >>> singleton_obj1 = YourClass()
    >>> singleton_obj2 = YourClass()
    >>> singleton_obj1
    <__main__.YourClass object at 0x7fc8f1948970>
    >>> singleton_obj2
    <__main__.YourClass object at 0x7fc8f1948970>
  """
  # For better understanding of the below implementation, read this:
  # https://refactoring.guru/design-patterns/singleton/python/example
  _instances = {}
  _lock = threading.Lock()

  def __call__(cls, *args, **kwargs):
    """Callable instance of a class."""
    with cls._lock:
      if cls not in cls._instances:
        cls._instances[cls] = super().__call__(*args, **kwargs)
    return cls._instances[cls]
