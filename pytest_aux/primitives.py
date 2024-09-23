"""
GOAL
----
collect all obvious variants of code objects

USEFUL IDEAS
------------
- in tests
- could be clearly used in docstrings without needless defining
    assert get_bool(LAMBDA_EXX) is False

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


def FUNC_ALL(*args, **kwargs) -> bool:
    """
    return all(args) and all(kwargs.values())

    CREATED SPECIALLY FOR
    ---------------------
    funcs_aux.Valid.run as tests
    """
    return all(args) and all(kwargs.values())


def FUNC_ANY(*args, **kwargs) -> bool:
    """
    return any(args) or any(kwargs.values())

    CREATED SPECIALLY FOR
    ---------------------
    funcs_aux.Valid.run as tests
    """
    return any(args) or any(kwargs.values())


def FUNC_LIST_DIRECT(*args, **kwargs) -> list[Any]:
    """
    DIRECT LIST() for Args+Kwargs

    CREATED SPECIALLY FOR
    ---------------------
    funcs_aux.Valid.get_bool as test variant

    return list(args) + list(kwargs)
    """
    return list(args) + list(kwargs)


def FUNC_LIST_VALUES(*args, **kwargs) -> list[Any]:
    """
    LIST() values for Args+Kwargs.values()

    CREATED SPECIALLY FOR
    ---------------------
    funcs_aux.Valid.get_bool as test variant

    return list(args) + list(kwargs.values())
    """
    return list(args) + list(kwargs.values())


def FUNC_DICT(*args, **kwargs) -> dict[Any, Any | None]:
    """
    DIRECT DICT() for Args+Kwargs

    CREATED SPECIALLY FOR
    ---------------------
    funcs_aux.Valid.get_bool as test variant

    return like DICT(*args, **kwargs)
    """
    result = dict.fromkeys(args)
    result.update(kwargs)
    return result


def FUNC_EXX(*args, **kwargs) -> NoReturn:
    raise Exception("CALLABLE_EXX")


def FUNC_GEN(*args, **kwargs) -> Generator:
    yield from range(5)


# ---------------------------------------------------------------------------------------------------------------------
LAMBDA = lambda *args, **kwargs: None
LAMBDA_NONE = lambda *args, **kwargs: None
LAMBDA_TRUE = lambda *args, **kwargs: True
LAMBDA_FALSE = lambda *args, **kwargs: False

LAMBDA_ALL = lambda *args, **kwargs: FUNC_ALL(*args, **kwargs)
LAMBDA_ANY = lambda *args, **kwargs: FUNC_ANY(*args, **kwargs)

LAMBDA_LIST_DIRECT = lambda *args, **kwargs: FUNC_LIST_DIRECT(*args, **kwargs)
LAMBDA_LIST_VALUES = lambda *args, **kwargs: FUNC_LIST_VALUES(*args, **kwargs)
LAMBDA_DICT = lambda *args, **kwargs: FUNC_DICT(*args, **kwargs)

# LAMBDA_EXX = lambda *args, **kwargs: raise Exception("LAMBDA_EXX")      # raise=SyntaxError: invalid syntax
LAMBDA_EXX = lambda *args, **kwargs: FUNC_EXX()
# LAMBDA_GEN = lambda *args, **kwargs: yield from range(5)      # yield=SyntaxError: invalid syntax
LAMBDA_GEN = lambda *args, **kwargs: FUNC_GEN()


# =====================================================================================================================
class Exx(Exception):
    pass
INST_EXX = Exx()

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
class Cls:
    pass
INST = Cls()


class ClsEmpty:
    pass
INST_EMPTY = ClsEmpty()


# ---------------------------------------------------------------------------------------------------------------------
class ClsInitArgsKwargs:
    """
    GOAL
    ----
    just apply init with any args/kwargs
    so no Exception would raise in any case!
    in first idea it was not matter to keep them in instance but did it just in case

    CREATED SPECIALLY FOR
    ---------------------
    ClsBoolTrue/*False
    """
    ARGS: tuple
    KWARGS: dict

    def __init__(self, *args, **kwargs):
        self.ARGS = args
        self.KWARGS = kwargs


class ClsInitExx:
    def __init__(self, *args, **kwargs) -> NoReturn:
        raise Exception()


# ---------------------------------------------------------------------------------------------------------------------
class ClsCall:
    def __call__(self, *args, **kwargs) -> None:
        pass

    def meth(self, *args, **kwargs) -> None:
        """
        for other results like None/True/False/Exx use direct LAMBDA/FUNC_*! or wait special necessity.
        """
        pass
INST_CALL = ClsCall()


class ClsCallNone(ClsCall):
    pass
INST_CALL_NONE = ClsCallNone()


class ClsCallTrue:
    def __call__(self, *args, **kwargs) -> bool:
        return True
INST_CALL_TRUE = ClsCallTrue()


class ClsCallFalse:
    def __call__(self, *args, **kwargs) -> bool:
        return False
INST_CALL_FALSE = ClsCallFalse()


class ClsCallExx:
    def __call__(self, *args, **kwargs) -> NoReturn:
        raise Exception()
INST_CALL_EXX = ClsCallExx()


# ---------------------------------------------------------------------------------------------------------------------
class ClsBoolTrue(ClsInitArgsKwargs):
    """
    CREATED SPECIALLY FOR
    ---------------------
    funcs_aux.Valid.get_bool as test variant
    """
    def __bool__(self):
        return True
INST_BOOL_TRUE = ClsBoolTrue()


class ClsBoolFalse(ClsInitArgsKwargs):
    """
    CREATED SPECIALLY FOR
    ---------------------
    funcs_aux.Valid.get_bool as test variant
    """
    def __bool__(self):
        return False
INST_BOOL_FALSE = ClsBoolFalse()


class ClsBoolExx(ClsInitArgsKwargs):
    """
    CREATED SPECIALLY FOR
    ---------------------
    funcs_aux.Valid.get_bool as test variant
    """
    def __bool__(self):
        raise Exception()
INST_BOOL_EXX = ClsBoolExx()


# ---------------------------------------------------------------------------------------------------------------------
class ClsIterYield:
    """
    CONSTRAINTS
    -----------
    YIELD and RETURN all are acceptable!
    several iterations - work fine!

        class Cls:
        def __iter__(self):
            yield from range(3)
            # return iter(range(3))

        obj = Cls()
        for _ in range(2):
            print()
            for i in obj:
                print(i)
    """

    def __iter__(self):
        # RETURN VARIANTS ------------
        # return [1,2,3]  #TypeError: iter() returned non-iterator of type 'list'
        # return range(5)  #TypeError: iter() returned non-iterator of type 'range'
        # return iter([1,2,3])  #OK

        # YIELD VARIANTS ------------    - MOST PREFERRED!(seek would be reset all time to the beginning!!!)
        # yield from [1,2,3]  #OK
        yield from range(5)   #OK
INST_ITER_YIELD = ClsIterYield()


class ClsGen:
    """
    ClsIterNext!
    """
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
INST_GEN = ClsGen()


# ---------------------------------------------------------------------------------------------------------------------
class ClsEq:
    def __init__(self, val: Any = None, *args, **kwargs):
        self.VAL = val

    def __eq__(self, other):
        return other == self.VAL

    def __ne__(self, other):
        return other != self.VAL
INST_EQ = ClsEq()


class ClsEqTrue(ClsInitArgsKwargs):
    def __eq__(self, other):
        raise True
    def __ne__(self, other):
        raise False
INST_EQ_TRUE = ClsEqTrue()


class ClsEqFalse(ClsInitArgsKwargs):
    def __eq__(self, other):
        raise False
    def __ne__(self, other):
        raise True
INST_EQ_FALSE = ClsEqFalse()


class ClsEqExx(ClsInitArgsKwargs):
    def __eq__(self, other):
        raise Exception()

    def __ne__(self, other):
        raise Exception()
INST_EQ_EXX = ClsEqExx()


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
    attrFuncList = FUNC_LIST_DIRECT
    attrFuncDict = FUNC_DICT
    attrFuncExx = FUNC_EXX
    attrFuncGen = FUNC_GEN

    attrGenCompr = GEN_COMPR

    attrCls = ClsEmpty
    attrInst = ClsEmpty()
    attrInstMeth = ClsCall().meth

    attrClsCall = ClsCall
    attrInstCall = ClsCall()
    attrClsCallTrue = ClsCallTrue
    attrInstCallTrue = ClsCallTrue()
    attrClsCallExx = ClsCallExx
    attrInstCallExx = ClsCallExx()

    attrClsIterYield = ClsIterYield
    attrInstIterYield = ClsIterYield()
    attrClsGen = ClsGen
    attrInstGen = ClsGen()

    attrClsBoolTrue = ClsBoolTrue
    attrInstBoolTrue = ClsBoolTrue()
    attrClsBoolFalse = ClsBoolFalse
    attrInstBoolFalse = ClsBoolFalse()
    attrClsBoolExx = ClsBoolExx
    attrInstBooExx = ClsBoolExx()

    attrSet = {1,2,3}
    attrList = [1,2,3]
    attrTuple = (1,2,3)
    attrDict = {1:1}
    attrListInst = [*[Cls(), ] * 3, 1]

    @property
    def propertyNone(self) -> None:
        return
    @classmethod
    @property
    def propertyClassmethodNone(cls) -> None:
        return

    @property
    def propertyInt(self) -> int:
        return 1
    @property
    def propertyExx(self) -> NoReturn:
        raise Exception("exxMsg")
    @property
    def propertyFunc(self) -> Callable:
        return FUNC

    def methNone(self) -> None:
        return
    def methInt(self) -> int:
        return 1
    def methExx(self) -> NoReturn:
        raise Exception("exxMsg")
    def methFunc(self) -> Callable:
        return FUNC
    @classmethod
    def classmethodNone(cls) -> None:
        return
    @staticmethod
    def staticmethodNone() -> None:
        return
INST_FULL_TYPES = ClsFullTypes()


# ---------------------------------------------------------------------------------------------------------------------
CALLABLE_LAMBDA = LAMBDA
CALLABLE_FUNC = FUNC

CALLABLE_CLS = ClsCall
CALLABLE_INST = ClsCall()

CALLABLE_METH_CLS = ClsFullTypes.methNone
CALLABLE_METH_CLS_CLASSMETHOD = ClsFullTypes.classmethodNone
CALLABLE_METH_CLS_STATICMETHOD = ClsFullTypes.staticmethodNone
CALLABLE_METH_CLS_PROPERTY = ClsFullTypes.propertyNone
CALLABLE_METH_CLS_PROPERTY_CLASSMETHOD = ClsFullTypes.propertyClassmethodNone

CALLABLE_METH_INST = ClsFullTypes().methNone
CALLABLE_METH_INST_CLASSMETHOD = ClsFullTypes().classmethodNone
CALLABLE_METH_INST_STATICMETHOD = ClsFullTypes().staticmethodNone
CALLABLE_METH_INST_PROPERTY = ClsFullTypes().propertyNone
CALLABLE_METH_INST_PROPERTY_CLASSMETHOD = ClsFullTypes().propertyClassmethodNone


# =====================================================================================================================
