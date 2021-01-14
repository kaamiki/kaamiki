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

"""Collection of all the constants traversing through implementation"""

import getpass
import pathlib
import sys

# Implementation identity.
__NAME = 'kaamiki'
__CODENAME = 'miroslava'

# The implementation adheres to Semantic Versioning Specification
# (SemVer) starting with version 0.0.1.
# You can read about it here: https://semver.org/spec/v2.0.0.html
__VERSION = '0.0.2'

# Implementation authors and project details.
__AUTHOR = 'Kaamiki Development Team'
__MAINTAINER = 'xames3'
__AUTHOR_EMAIL = __MAINTAINER_EMAIL = 'xames3.kaamiki@gmail.com'
__URL = 'https://github.com/kaamiki/kaamiki'
__LICENSE = 'Apache Software License 2.0'
__DESCRIPTION = (
    'Kaamiki is a simple cross-platform automation framework for data '
    'science and machine learning tasks.'
)

# Current operating system and session user.
__OS = sys.platform
__SESSION = getpass.getuser()

# Encoding for all StringIO and FileIO operations.
ENCODING = 'utf-8'

# Separator for string substitution.
SUBSTITUTE = '_'

# File system separator.
__SEP = pathlib.os.sep

# Default canonical and sub directories for the implementation
ROOT_DIR = pathlib.Path().home() / __NAME
LOGS_DIR = ROOT_DIR / __SESSION / 'logs'
