#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
complexity.prep
---------------

Functions for preparing a Complexity project for static site generation,
before it actually happens.
"""

import os
import shutil

from . import utils


def prompt_and_delete_cruft(output_dir):
    """
    Asks if it's okay to delete `output_dir/`.
    If so, go ahead and delete it.

    :param output_dir: The Complexity output directory, e.g. `www/`.
    :paramtype output_dir: directory
    """
    if not os.path.exists(output_dir):
        return True

   
    shutil.rmtree(output_dir)
    return True
