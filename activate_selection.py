import maya.api.OpenMaya as om


def activate_selection(selection):
    """
    Activates the given selection

    Parameters
    ----------
    selection : MSelectionList
        the selected object

    Returns
    -------
    None
    """
    
    om.MGlobal.setActiveSelectionList(selection)
