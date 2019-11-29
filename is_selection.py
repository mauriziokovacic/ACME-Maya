import maya.api.OpenMaya as om
from .is_type import *


def is_selection(*obj):
    """
    Returns whether or not all the inputs are MSelectionLists

    Parameters
    ----------
    *obj : object...
        a sequence of objects

    Returns
    -------
    bool
        True if the inputs are MSelectionLists, False otherwise
    """

    return is_type(om.MSelectionList, *obj)
