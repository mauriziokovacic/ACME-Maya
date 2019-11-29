from .export_OBJ import *
from .FrameCtrl  import *


def export_frames(object, frames, name='Object', path=os.getcwd()):
    """
    Exports the specified frames of the given object

    Parameters
    ----------
    object : ...
        the object to export
    frames : list
        the list of frames to export
    name : str (optional)
        the common name part for the exported frames (default is 'Object')
    path : str (optional)
        the path to export the object to (default is os.getcwd())

    Returns
    -------
    None
    """

    anim = FrameCtrl()
    f = anim.current
    for frame in frames:
        anim.current = frame
        export_OBJ(object, name=name + str(frame), path=path)
    anim.current = f
