import maya.api.OpenMaya as om


def time2frame(value):
    """
    Converts a maya MTime object into its frame number

    Parameters
    ----------
    value : MTime
        the maya MTime object

    Returns
    -------
    int
        the frame number
    """

    return int(value.asUnits(om.MTime.kFilm))
