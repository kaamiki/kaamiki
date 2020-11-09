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
Kaamiki Exceptions

Collection of all the exceptions raised by various kaamiki operations.
"""


def this_is_effing_bug() -> str:
  """Return bug report warning."""
  title = "YIKES! There's a bug:"
  title += "".join(["\n", "-" * len(title)])
  return ("\n\n{}\nIf you are seeing this, then there is something wrong with "
          "Kaamiki and not your code!\nPlease report this issue immediately "
          "here: \"https://github.com/kaamiki/kaamiki/issues/new\"\nso that "
          "we can fix the issue at the earliest. It would be a great help if "
          "you could provide\nthe steps, traceback information or even a "
          "sample code for reproducing this bug while\nsubmitting an issue."
          "\n").format(title)


class KaamikiError(Exception):
  """Base exception class for all kaamiki related exceptions."""

  def __init__(self, message: str, okay: bool, **kwargs):
    if not okay:
      message += this_is_effing_bug()
    super().__init__(message)
    self.message = message
    for key, value in kwargs.items():
      setattr(self, key, value)

  def __str__(self):
    return self.message.format(**vars(self))


class UnsupportedFileType(KaamikiError):
  """Exception to be raised when dealing with unsupported file types."""

  def __init__(
          self,
          message: str = "FileIO operation not supported by {suffix!r} file",
          **kwargs):
    super().__init__(message, **kwargs)
