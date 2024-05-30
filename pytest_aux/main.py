import pathlib
from typing import *
import pytest

from object_info import *
from pytest import mark


# =====================================================================================================================
pass


# =====================================================================================================================
def pytest_parametrisation_tester(
        func_link, args, kwargs, _EXPECTED,
        _MARK: pytest.MarkDecorator | None  = None,
        _COMMENT: str | None = None
):
    args = args or ()
    kwargs = kwargs or {}
    comment = _COMMENT or ""

    try:
        actual_value = func_link(*args, **kwargs)
    except Exception as exx:
        actual_value = exx

    # MARKS -------------------------
    print(f"{mark.skipif(True)=}")
    if _MARK == mark.skip:
        pytest.skip("skip")
    elif isinstance(_MARK, pytest.MarkDecorator) and _MARK.name == "skipif" and all(_MARK.args):
        pytest.skip("skipIF")

    if _MARK == mark.xfail:
        if TypeChecker.check__exception(_EXPECTED):
            assert not TypeChecker.check__nested__by_cls_or_inst(actual_value, _EXPECTED), f"[xfail]{comment}"
        else:
            assert actual_value != _EXPECTED, f"[xfail]{comment}"
    else:
        if TypeChecker.check__exception(_EXPECTED):
            assert TypeChecker.check__nested__by_cls_or_inst(actual_value, _EXPECTED)
        else:
            assert actual_value == _EXPECTED


# =====================================================================================================================
