"""
here i wish to collect all available variants useful in tests
"""
# ---------------------------------------------------------------------------------------------------------------------
from typing import *


# =====================================================================================================================
def FUNC(*args, **kwargs) -> None:
    pass


def FUNC_NONE(*args, **kwargs) -> None:
    return None


def FUNC_TRUE(*args, **kwargs) -> bool:
    return True


def FUNC_FALSE(*args, **kwargs) -> bool:
    return False


def FUNC_EXX(*args, **kwargs) -> NoReturn:
    raise Exception("CALLABLE_EXX")


# ---------------------------------------------------------------------------------------------------------------------
LAMBDA = lambda *args, **kwargs: None
LAMBDA_NONE = lambda *args, **kwargs: None
LAMBDA_TRUE = lambda *args, **kwargs: True
LAMBDA_FALSE = lambda *args, **kwargs: False
# LAMBDA_EXX = lambda *args, **kwargs: raise Exception("LAMBDA_EXX")      # SyntaxError: invalid syntax
LAMBDA_EXX = lambda *args, **kwargs: FUNC_EXX()


# =====================================================================================================================
class Exx(Exception):
    pass


# ---------------------------------------------------------------------------------------------------------------------
# class ClsBool(bool):  # cant use it!
#     pass


class ClsInt(int):
    pass


class ClsFloat(float):
    pass


class ClsStr(str):
    pass


class ClsList(list):
    pass


class ClsSet(set):
    pass


class ClsDict(dict):
    pass


# =====================================================================================================================
class ClsEmpty:
    pass


class ClsCallable:
    def __call__(self, *args, **kwargs):
        pass

    def meth(self, *args, **kwargs):
        pass


class ClsFullTypes:
    attrZero = 0

    attrNone = None
    attrTrue = True
    attrFalse = False
    attrInt = 1
    attrFloat = 1.1
    attrStr = "str"
    attrBytes = b"bytes"

    attrFunc = FUNC
    attrFuncTrue = FUNC_TRUE

    attrCls = ClsEmpty
    attrInst = ClsEmpty()
    attrInstMeth = ClsCallable().meth
    attrInstCallable = ClsCallable()

    attrSet = {1,2,3}
    attrList = [1,2,3]
    attrTuple = (1,2,3)
    attrDict = {1:1}
    attrListInst = [*[ClsEmpty(), ] * 3, 1]
    @property
    def propertyInt(self) -> int:
        return 1
    @property
    def propertyExx(self) -> NoReturn:
        raise Exception("exxMsg")
    @property
    def propertyFunc(self) -> Callable:
        return FUNC
    def methInt(self) -> int:
        return 1
    def methExx(self) -> NoReturn:
        raise Exception("exxMsg")
    def methFunc(self) -> Callable:
        return FUNC


# =====================================================================================================================
