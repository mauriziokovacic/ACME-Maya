import maya.api.OpenMaya as om


def active_selection():
    """
    Returns the current active selection

    Returns
    -------
    MSelectionList
        the current active selection
    """

    om.MGlobal.getActiveSelectionList()
