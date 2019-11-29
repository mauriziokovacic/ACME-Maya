import maya.api.OpenMaya as om


def frame2time(frame):
    """
    Converts a given frame number into a maya MTime object

    Parameters
    ----------
    frame : int
        the frame number

    Returns
    -------
    MTime
        a maya MTime object
    """
    
    return om.MTime(frame, unit=om.MTime.kFilm)
