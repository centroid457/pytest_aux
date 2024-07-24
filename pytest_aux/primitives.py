"""
here i wish to collect all available variants useful in tests
"""
# ---------------------------------------------------------------------------------------------------------------------
from typing import *


# =====================================================================================================================
GEN_COMPR = (i for i in range(3))


# ---------------------------------------------------------------------------------------------------------------------
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


def FUNC_GEN(*args, **kwargs) -> Generator:
    yield from range(5)


# ---------------------------------------------------------------------------------------------------------------------
LAMBDA = lambda *args, **kwargs: None
LAMBDA_NONE = lambda *args, **kwargs: None
LAMBDA_TRUE = lambda *args, **kwargs: True
LAMBDA_FALSE = lambda *args, **kwargs: False
# LAMBDA_EXX = lambda *args, **kwargs: raise Exception("LAMBDA_EXX")      # raise=SyntaxError: invalid syntax
LAMBDA_EXX = lambda *args, **kwargs: FUNC_EXX()
# LAMBDA_GEN = lambda *args, **kwargs: yield from range(5)      # yield=SyntaxError: invalid syntax
LAMBDA_GEN = lambda *args, **kwargs: FUNC_GEN()


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


class ClsIterable:
    def __iter__(self):
        yield from range(5)


class ClsGen:
    def __init__(self, start=1, end=3):
        self.start = start
        self.end = end
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.end:
            raise StopIteration
        else:
            result = self.current
            self.current += 1
            return result


# ---------------------------------------------------------------------------------------------------------------------
class ClsEq:
    def __init__(self, val: Any = None):
        self.VAL = val

    def __eq__(self, other):
        return other == self.VAL


class ClsEqExx:
    def __eq__(self, other):
        raise Exception()


# ---------------------------------------------------------------------------------------------------------------------
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
    attrFuncExx = FUNC_EXX
    attrFuncGen = FUNC_GEN

    attrGenCompr = GEN_COMPR

    attrCls = ClsEmpty
    attrInst = ClsEmpty()
    attrInstMeth = ClsCallable().meth
    attrClsCallable = ClsCallable
    attrInstCallable = ClsCallable()
    attrClsIterable = ClsIterable
    attrInstIterable = ClsIterable()
    attrClsGen = ClsGen
    attrInstGen = ClsGen()

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
