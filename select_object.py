import maya.api.OpenMaya as om


def select_object(name=None):
    """
    Selects the objects specified by the given name

    Parameters
    ----------
    name : str (optional)
        the name of the object to select. If None the active object will be selected (default is None)

    Returns
    -------
    MSelectionList
        the selected object

    Raises
    ------
    RuntimeError
        if no object with the specified name is found
    """

    if name is None:
        selection = om.MGlobal.getActiveSelectionList()
    else:
        selection = om.MSelectionList()
        selection.add(name)
    return selection
