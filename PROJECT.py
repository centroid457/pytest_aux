from typing import *
from _aux__release_files import release_files_update


# =====================================================================================================================
# VERSION = (0, 0, 3)   # 1/deprecate _VERSION_TEMPLATE from PRJ object +2/place update_prj here in __main__ +3/separate finalize attrs
VERSION = (0, 0, 4)     # add AUTHOR_NICKNAME_GITHUB for badges


# =====================================================================================================================
class PROJECT:
    # AUTHOR -----------------------------------------------
    AUTHOR_NAME: str = "Andrei Starichenko"
    AUTHOR_EMAIL: str = "centroid@mail.ru"
    AUTHOR_HOMEPAGE: str = "https://github.com/centroid457/"
    AUTHOR_NICKNAME_GITHUB: str = "centroid457"

    # PROJECT ----------------------------------------------
    NAME_IMPORT: str = "pytest_aux"
    KEYWORDS: list[str] = [
        "pytest templates", "pytest examples", "pytest aux", "pytest parametrisation",
        "pytest useful funcs",
        "testing objects set",
    ]
    CLASSIFIERS_TOPICS_ADD: list[str] = [
        # "Topic :: Communications",
        # "Topic :: Communications :: Email",
    ]

    # README -----------------------------------------------
    # add DOUBLE SPACE at the end of all lines! for correct representation in MD-viewers
    DESCRIPTION_SHORT: str = "templates/examples and aux for pytest"
    DESCRIPTION_LONG: str = """designed for ..."""
    FEATURES: list[str] = [
        # "feat1",
        # ["feat2", "block1", "block2"],

        "parametrisation usage example + aux",
        "testing objects - primitives for testing different types",
    ]

    # HISTORY -----------------------------------------------
    VERSION: tuple[int, int, int] = (0, 0, 14)
    TODO: list[str] = [
        "..."
    ]
    FIXME: list[str] = [
        "..."
    ]
    NEWS: list[str] = [
        "[PRIMITIVES] add/move here from all other modules",
    ]

    # FINALIZE -----------------------------------------------
    VERSION_STR: str = ".".join(map(str, VERSION))
    NAME_INSTALL: str = NAME_IMPORT.replace("_", "-")


# =====================================================================================================================
if __name__ == '__main__':
    release_files_update(PROJECT)


# =====================================================================================================================
