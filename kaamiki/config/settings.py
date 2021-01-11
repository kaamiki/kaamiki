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

"""Kaamiki's default settings and attributes."""

import os.path as _os
import pathlib
import platform

# NOTE: PACKAGING DETAILS
# These attributes are used in the setup and for maintaining, packaging
# and publishing the package on PyPI and GitHub respectively. These
# attributes are not meant to be modified by anyone but the authors.
# The below attribute shall never be changed by anyone, EVER!
MARK_I = 'Charlotte'

# This is the name of the concept and the framework. The name is
# purposely defined here so that it propagates in places where the
# title is expected.
MARK_II = 'kaamiki'

# The framework adheres to Semantic Versioning Specification (SemVer)
# starting with version 0.0.1.
# You can read about it here: https://semver.org/spec/v2.0.0.html
# The version should be timely updated as progress is made.
FRAMEWORK_VERSION = '0.0.2'

# Author details. Since the framework is built with open source in
# mind, it is better to put all the authors, co-authors and
# contributors under the same umbrella.
AUTHOR = 'Kaamiki Development Team'
AUTHOR_EMAIL = 'xames3.kaamiki@gmail.com'

# Maintainer details, count of the below folks should probably
# increase in future, ** fingers cross **
MAINTAINER = 'xames3'
MAINTAINER_EMAIL = AUTHOR_EMAIL

# This is where all the entire source code, documentation, updates and
# bug reports will be hosted.
FRAMEWORK_URL = 'https://github.com/kaamiki/kaamiki'

# Open source software license used to publish the framework.
# Please note that the commented out header license should be involved
# in each and every valid module as it packs the terms and copyrights.
OSS_LICENSE = 'Apache Software License 2.0'

# One liner description of the framework. The description is bound
# to change as the progress is made.
SHORT_DESCRIPTION = ('Kaamiki is a simple cross-platform automation '
                     'framework for data science and machine learning tasks.')

# Flag which raises warning if the installed version of the framework
# is either outdated or a nightly (development) build.
# 0 = Fresh install or Update to the existing build.
# 1 = Checked build
# 2 = Beta (nightly build)
# NOTE(xames3): Check and update mechanism is missing, must be added.
INSTALLATION_STATUS = 0

# NOTE: USER AND OS DETAILS
# These attributes are used for user and/or operating system specific
# details. These attributes are read-only and cannot be altered by user.
# Current operating system name. This information is traversed through
# the entire framework for intermediate checks for optimizing workflows.
OS = platform.system()

# NOTE: DATETIME AND TIMEZONE DETAILS
# These attributes deal with all the datetime and related parameters.
# They are accessible and meant to be updated by the user as per the
# requirements. 
# Default time zone to be used if the choosing local time zone is not
# an available option. This parameter can be overridden by the user.
DEF_TZONE = 'UTC'

# If set to True, local time zone for the user will be used. This flag
# assumes that all the date time related events are handled in UTC by
# default.
USE_LOCAL_TZONE = False

# NOTE: SYSTEM LEVEL CONSTANTS
# These attributes are set of generic constants that are fairly the
# same for all development purposes. These can be accessed and modified
# by the user as required.
# Default encoding standard to use for all StringIO operations.
DEF_ENCODING = 'utf-8'

# Default separator for string substitution.
DEF_STRING_SEP = '_'

# NOTE: FILE SYSTEM AND PATH DETAILS
# These attributes are mainly related to the file name, file path,
# file system, etc. These are accessible throughout the system as they
# traverse for respective use cases.
# Default separator for pathnames.
DEF_PATH_SEP = _os.sep

# Default directory for all framework related activities like logging,
# data acquisition and caching. This directory can be overridden by the
# user if needed.
DEF_ROOT_DIR = pathlib.Path().home() / MARK_II

# All log events are recorded in `LOGS_DIR` by default, if not being
# overridden by the user settings. Kaamiki doesn't log errors
# separately!
DEF_LOGS_DIR = DEF_ROOT_DIR / 'logs'
