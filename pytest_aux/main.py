import pathlib
from typing import *
import pytest

from object_info import *
from funcs_aux import *
from pytest import mark


# =====================================================================================================================
pass


# =====================================================================================================================
def pytest_func_tester(
        func_link: Union[Callable[..., Union[Any, NoReturn]], Any], # if func would get Exx - instance of exx would be returned for value!
        args: Union[tuple[Any], Any] = Value_NotPassed,
        kwargs: Optional[dict[str, Any]] = None,
        _EXPECTED: Union[Any, Exception, Type[Exception]] = True,  # EXACT VALUE OR ExxClass

        _MARK: pytest.MarkDecorator | None = None,
        _COMMENT: str | None = None
) -> NoReturn | None:
    """
    function which test target func with exact parameters
    :return: Exception only on AssertionError, no exception withing target func!
    """
    if TypeChecker.check__nested__by_cls_or_inst(args, Value_NotPassed):    # DONT CHANGE just to "args == Value_NotPassed"!!! see tests!!!
        args = ()
    if not isinstance(args, tuple):
        args = (args, )
    kwargs = kwargs or dict()
    comment = _COMMENT or ""

    if TypeChecker.check__func_or_meth(func_link):
        try:
            actual_value = func_link(*args, **kwargs)
        except Exception as exx:
            actual_value = exx
    else:
        actual_value = func_link

    print(f"pytest_func_tester={args=}/{kwargs=}//{actual_value=}/{_EXPECTED=}")

    # MARKS -------------------------
    # print(f"{mark.skipif(True)=}")
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


# ---------------------------------------------------------------------------------------------------------------------
def pytest_func_tester__no_args_kwargs(
        func_link,
        _EXPECTED = True,

        _MARK = None,
        _COMMENT = None
) -> NoReturn | None:
    """
    created specially for using inline operators like 'func_link=A>=B'

    CAREFUL
    -------
    BUT be careful cause of exceptions!
    recommended using pytest_func_tester__no_args instead with 'func_link=lambda: A>=B'!!!
    """
    pytest_func_tester(func_link=func_link, _EXPECTED=_EXPECTED, _MARK=_MARK, _COMMENT=_COMMENT)


# ---------------------------------------------------------------------------------------------------------------------
def pytest_func_tester__no_kwargs(
        func_link,
        args,
        _EXPECTED = True,

        _MARK = None,
        _COMMENT = None
) -> NoReturn | None:
    """
    short variant in case of kwargs is not needed

    WHY IT NEED
    -----------
    params passed by pytest while parametrisation as TUPLE!!!! so you cant miss any param in the middle!
    """
    pytest_func_tester(func_link=func_link, args=args, _EXPECTED=_EXPECTED, _MARK=_MARK, _COMMENT=_COMMENT)


# ---------------------------------------------------------------------------------------------------------------------
def pytest_func_tester__no_args(
        func_link,
        kwargs,
        _EXPECTED = True,

        _MARK = None,
        _COMMENT = None
) -> NoReturn | None:
    """
    short variant in case of args is not needed
    """
    pytest_func_tester(func_link=func_link, kwargs=kwargs, _EXPECTED=_EXPECTED, _MARK=_MARK, _COMMENT=_COMMENT)


# =====================================================================================================================
pass    # USAGE EXAMPLES ----------------------------------------------------------------------------------------------
pass    # USAGE EXAMPLES ----------------------------------------------------------------------------------------------
pass    # USAGE EXAMPLES ----------------------------------------------------------------------------------------------
pass    # USAGE EXAMPLES ----------------------------------------------------------------------------------------------
pass    # USAGE EXAMPLES ----------------------------------------------------------------------------------------------
pass    # USAGE EXAMPLES ----------------------------------------------------------------------------------------------
pass    # USAGE EXAMPLES ----------------------------------------------------------------------------------------------
pass    # USAGE EXAMPLES ----------------------------------------------------------------------------------------------
pass    # USAGE EXAMPLES ----------------------------------------------------------------------------------------------
pass    # USAGE EXAMPLES ----------------------------------------------------------------------------------------------
pass    # USAGE EXAMPLES ----------------------------------------------------------------------------------------------
pass    # USAGE EXAMPLES ----------------------------------------------------------------------------------------------
pass    # USAGE EXAMPLES ----------------------------------------------------------------------------------------------
pass    # USAGE EXAMPLES ----------------------------------------------------------------------------------------------
pass    # USAGE EXAMPLES ----------------------------------------------------------------------------------------------


def _func_example(arg1: Any, arg2: Any) -> str:
    return f"{arg1}{arg2}"


# =====================================================================================================================
@pytest.mark.parametrize(argnames="func_link", argvalues=[_func_example, ])
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
        # ((1, 2), {}, "12", mark.xfail, "SHOULD BE FAIL!"),
    ]
)
def test__full_params(func_link, args, kwargs, _EXPECTED, _MARK, _COMMENT):     # NOTE: all params passed by TUPLE!!!! so you cant miss any in the middle!
    pytest_func_tester(func_link, args, kwargs, _EXPECTED, _MARK, _COMMENT)


# =====================================================================================================================
@pytest.mark.parametrize(argnames="func_link", argvalues=[int, ])
@pytest.mark.parametrize(
    argnames="args, kwargs, _EXPECTED",
    argvalues=[
        (("1", ), {}, 1),
        ("1", {}, 1),                   # ARGS - direct one value acceptable
        (("hello", ), {}, Exception),   # EXPECT - direct exceptions
    ]
)
def test__short_variant(func_link, args, kwargs, _EXPECTED):
    pytest_func_tester(func_link, args, kwargs, _EXPECTED)


# =====================================================================================================================
@pytest.mark.parametrize(argnames="func_link", argvalues=[int, ])
@pytest.mark.parametrize(
    argnames="args, _EXPECTED",
    argvalues=[
        (("1", ), 1),
        ("1", 1),
        ("", ValueError),
        (("hello", ), Exception),
    ]
)
def test__shortest_variant(func_link, args, _EXPECTED):
    pytest_func_tester__no_kwargs(func_link, args, _EXPECTED)


# =====================================================================================================================
@pytest.mark.parametrize(
    argnames="expression",
    argvalues=[
        ("1rc2") == "1rc2",
        ("1rc2") != "1rc1",

        ("1.1rc2") > "1.0rc1",
        ("1.1rc2") > "1.1rc0",
        ("1.1rc2.0") > "1.1rc2",

        # ("01.01rc02") > "1.1rc1",
        ("01.01rc02") < "1.1rd1",
    ]
)
def test__expressions(expression):
    pytest_func_tester__no_args_kwargs(expression)


# =====================================================================================================================
