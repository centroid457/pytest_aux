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
def func_example(arg1: Any, arg2: Any) -> str:
    return f"{arg1}{arg2}"


# =====================================================================================================================
@pytest.mark.parametrize(
    argnames="p1,p2,_EXPECTED,_MARK",
    argvalues=[
        # TRIVIAL -------------
        (1, None, "1None", None),
        (1, 2, "12", None),

        # LIST -----------------
        (1, [], "1[]", None),

        # MARKS -----------------
        (1, 2, None, mark.skip),
        (1, 2, None, mark.skipif(True)),
        (1, 2, None, mark.skipif(False)),
        (1, 2, None, mark.xfail),
        (1, 2, "12", mark.xfail),
    ]
)
def test__example_simple__without_templating(p1, p2, _EXPECTED, _MARK):
    func_link = func_example
    try:
        value_actual = func_link(arg1=p1, arg2=p2)
    except Exception as exx:
        value_actual = exx

    # MARKS -------------------------
    print(f"{mark.skipif(True)=}")
    if _MARK == mark.skip:
        pytest.skip()
    elif isinstance(_MARK, pytest.MarkDecorator) and _MARK.name == "skipif" and all(_MARK.args):
        pytest.skip()
    elif _MARK == mark.xfail:
        assert value_actual != _EXPECTED
    else:
        assert value_actual == _EXPECTED


# =====================================================================================================================
# =====================================================================================================================
# =====================================================================================================================
# =====================================================================================================================
# =====================================================================================================================
@pytest.mark.parametrize(
    argnames="args, kwargs, _EXPECTED, _MARK, _COMMENT",
    argvalues=[
        # TRIVIAL -------------
        ((1, None), {}, "1None", None, "ok"),
        ((1, 2), {}, "12", None, "ok"),

        # LIST -----------------
        ((1, []), {}, "1[]", None, "ok"),

        # MARKS -----------------
        ((1, 2), {}, None, mark.skip, "skip"),
        ((1, 2), {}, None, mark.skipif(True), "skip"),
        ((1, 2), {}, "12", mark.skipif(False), "ok"),
        ((1, 2), {}, None, mark.xfail, "ok"),
        ((1, 2), {}, "12", mark.xfail, "SHOULD BE FAIL!"),
    ]
)
@pytest.mark.parametrize(argnames="func_link", argvalues=[func_example, ])
def test__with_comments(func_link, args, kwargs, _EXPECTED, _MARK, _COMMENT):
    pytest_func_tester(func_link, args, kwargs, _EXPECTED, _MARK, _COMMENT)


# =====================================================================================================================
@pytest.mark.parametrize(argnames="func_link", argvalues=[int, ])
@pytest.mark.parametrize(
    argnames="args, kwargs, _EXPECTED",
    argvalues=[
        (("1", ), {}, 1),
        (("hello", ), {}, Exception),
    ]
)
def test__short_variant(func_link, args, kwargs, _EXPECTED):
    pytest_func_tester(func_link, args, kwargs, _EXPECTED)


# =====================================================================================================================
