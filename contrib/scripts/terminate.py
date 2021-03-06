#!/usr/bin/python3
#    This file is part of GNUnet.
#    (C) 2011, 2018 Christian Grothoff (and other contributing authors)
#
#    GNUnet is free software: you can redistribute it and/or modify it
#    under the terms of the GNU Affero General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    GNUnet is distributed in the hope that it will be useful, but
#    WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
#    Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#    SPDX-License-Identifier: AGPL3.0-or-later
#
# Utility module that implements safe process termination for W32.
# For other platforms it's equivalent to Popen.kill ()
# Requires pywin32 on W32.

import sys
import subprocess
import os


class dummyobj(object):
    pass


def safe_terminate_process_by_pid(pid, code):
    # XXX (F821): Undefined name 'SIGKILL'
    return os.kill(int(pid), SIGKILL)


def safe_terminate_process(proc, code):
    return proc.kill()
