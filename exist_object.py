import maya.api.OpenMaya as om


def exist_object(name):
    """
    Returns True if an object with the specified name exists, False otherwise

    Parameters
    ----------
    name : str
        the name of the object to check

    Returns
    -------
    bool
        True if an object with the specified name exists, False otherwise
    """

    selection = om.MSelectionList()
    try:
        selection.add(name)
    except:
        return False
    return True
