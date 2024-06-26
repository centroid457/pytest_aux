from typing import *
import pytest

import pathlib

from pytest import mark
from funcs_aux import *
from classes_aux import *


# =====================================================================================================================
# KEEP FILES IN ROOT! OR IMPORT PRJ_MODULE WOULD FROM SYSTEM! NOT THIS SOURCE!!!
# if you will start tests directly in IDE - it will start and work correctly from CURRENT SOURCE!
# but if you will start in CMD/PYTEST - it would work from PYPI!!!
from pytest_aux import *


# =====================================================================================================================
class Cls(CmpInst):
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
@pytest.mark.parametrize(
    argnames="func_link, args, kwargs, _EXPECTED, _pytestExpected",
    argvalues=[
        # not callable ------------
        (True, Value_NotPassed, None, True, True),
        (True, 111, {111: 222}, True, True),
        (False, Value_NotPassed, {}, True, False),

        # callable ------------
        (lambda value: value, Value_NotPassed, {}, True, False),

        (lambda value: value, None, {}, True, False),
        (lambda value: value, None, {}, None, True),
        (lambda value: value, True, {}, True, True),
        (lambda value: value, (True, ), {}, True, True),
        (lambda value: value, Value_NotPassed, {"value": True}, True, True),
        (lambda value: value, Value_NotPassed, {"value": None}, True, False),
    ]
)
def test__pytest_func_tester(func_link, args, kwargs, _EXPECTED, _pytestExpected):
    try:
        pytest_func_tester(func_link=func_link, args=args, kwargs=kwargs, _EXPECTED=_EXPECTED)
    except:
        assert not _pytestExpected
    else:
        assert _pytestExpected


# =====================================================================================================================
