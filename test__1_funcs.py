from typing import *
import pytest

import pathlib
import shutil
from tempfile import TemporaryDirectory

from pytest import mark
from funcs_aux import *


# =====================================================================================================================
# KEEP FILES IN ROOT! OR IMPORT PRJ_MODULE WOULD FROM SYSTEM! NOT THIS SOURCE!!!
from pytest_aux import *


# =====================================================================================================================
# TODO: add tests for funcs!!!


class Cls(Cmp):
    def __init__(self, value):
        self.VALUE = value

    def __cmp__(self, other):
        other = Cls(other)
        if self.VALUE == other.VALUE:
            return 0
        if self.VALUE > other.VALUE:
            return 1
        if self.VALUE < other.VALUE:
            return -1


def test____LE__():
    pytest_func_tester__no_kwargs(func_link=lambda result: result == 1, args=Cls(1), _EXPECTED=True)


# =====================================================================================================================
