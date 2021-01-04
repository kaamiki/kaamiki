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

"""Kaamiki's filesystem based validations."""

import errno
import os
import os.path as _os
from pathlib import Path
from typing import Union

from kaamiki.utils.exceptions import InvalidDirectoryName

__all__ = ['validate_dirname']

_SEP = _os.sep

# Windows specific system error codes can be found here:
# https://docs.microsoft.com/en-us/windows/win32/debug/system-error-codes--0-499-
_ERROR_INVALID_NAME = 123


def validate_dirname(dirname: Union[Path, str]) -> bool:
    """
    Check whether the provided directory name is valid or not. This is
    done by considering each part of dirname and testing if it is valid
    or not, ignoring non-existent and non-readable path components.

    Returns True if the dirname is valid for current OS else False.
    """
    if not isinstance(dirname, (Path, str)) or not dirname:
        return False
    if _os.isfile(dirname):
        raise FileExistsError(f'File: {dirname!r} already exists')
    try:
        _, dirname = _os.splitdrive(dirname)
        home = os.environ.get('HOMEDRIVE', 'C:') if os.name == 'nt' else _SEP
        assert _os.isdir(home)
        home = home.rstrip(_SEP) + _SEP
        for part in dirname.split(_SEP):
            try:
                os.lstat(home + part)
            except OSError as err:
                if hasattr(err, 'winerror'):
                    # pyright: reportGeneralTypeIssues=false
                    if err.winerror == _ERROR_INVALID_NAME:
                        raise InvalidDirectoryName(
                            valid=True,
                            msg=f'Path: {dirname!r} syntax is incorrect'
                        )
                elif err.errno in (errno.ENAMETOOLONG, errno.ERANGE):
                    raise InvalidDirectoryName(
                        valid=True,
                        msg=f'Path: {dirname!r} is too long for a directory'
                    )
    except TypeError:
        return False
    else:
        return True
