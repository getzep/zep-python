from enum import Enum
from typing import Any, Dict


class SearchType(str, Enum):
    similarity = "similarity"
    mmr = "mmr"


def filter_dict(d: Dict[Any, Any]) -> Dict[Any, Any]:
    """
    Filters out None values from a dictionary.

    Parameters
    ----------
    d : Dict[Any, Any]
        The dictionary to be filtered.

    Returns
    -------
    Dict[Any, Any]
        The filtered dictionary.
    """
    return {k: v for k, v in d.items() if v is not None}
