from .linspace import *


def arange(start, end):
    """
    Returns a list of n even spaced scalars in range [start, end]

    Parameters
    ----------
    start : int or float
        the starting value
    end : int or float
        the ending value

    Returns
    -------
    list
        a list of n ints in range [start, end]
    """

    return linspace(start, end, abs(start-end), dtype=int)
