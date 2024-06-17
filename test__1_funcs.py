from typing import *
import pytest

import pathlib
import shutil
from tempfile import TemporaryDirectory

from pytest import mark


# =====================================================================================================================
# KEEP FILES IN ROOT! OR IMPORT PRJ_MODULE WOULD FROM SYSTEM! NOT THIS SOURCE!!!
from pytest_aux import *


# =====================================================================================================================
# TODO: add tests for funcs!!!


class Cls:
    def __init__(self, value):
        self.VALUE = value

    def __cmp(self, other):
        other = Cls(other)
        if self.VALUE == other.VALUE:
            return 0
        if self.VALUE > other.VALUE:
            return 1
        if self.VALUE < other.VALUE:
            return -1

    def __eq__(self, other):
        return self.__cmp(other) == 0

    def __ne__(self, other):
        return self.__cmp(other) != 0

    def __lt__(self, other):
        return self.__cmp(other) < 0

    def __gt__(self, other):
        return self.__cmp(other) > 0

    def __le__(self, other):
        return self.__cmp(other) <= 0

    def __ge__(self, other):
        return self.__cmp(other) >= 0


def test____LE__():
    pytest_func_tester__no_kwargs(func_link=lambda result: result == 1, args=Cls(1), _EXPECTED=True)


# =====================================================================================================================
