# Copyright (c) Facebook, Inc. and its affiliates.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.
##############################################################################

"""Environment helper functions."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import os
import sys
import yaml

# Default value of the CMake install prefix
_CMAKE_INSTALL_PREFIX = '/usr/local'


def get_runtime_dir():
    """Retrieve the path to the runtime directory."""
    return sys.path[0]


def get_py_bin_ext():
    """Retrieve python binary extension."""
    return '.py'


def set_up_matplotlib():
    """Set matplotlib up."""
    import matplotlib
    # Use a non-interactive backend
    matplotlib.use('Agg')


def exit_on_error():
    """Exit from a detectron tool when there's an error."""
    sys.exit(1)


def import_nccl_ops():
    """Import NCCL ops."""
    # There is no need to load NCCL ops since the
    # NCCL dependency is built into the Caffe2 gpu lib
    pass

def get_detectron_ops_lib():
	print("In Windows, Detectron ops are built-in. No need to load dynamically. Ignore the following warning.")
	return ""

def get_custom_ops_lib():
	print("In Windows, Detectron custom ops are currently not supported. Ignore the following warning.")
	return ""
# YAML load/dump function aliases
yaml_load = yaml.load
yaml_dump = yaml.dump