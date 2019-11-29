import os
import maya.cmds as cmds
import maya.api.OpenMaya as om
from .active_selection   import *
from .activate_selection import *
from .is_selection       import *
from .emplace_directory  import *


def export_OBJ(object, name, path=os.getcwd()):
    """
    Exports the given object into an OBJ file with the given filename in the specified path

    Parameters
    ----------
    object : ...
        the object to export
    name : str
        the file name
    path : str (optional)
        the directory to export the object to

    Returns
    -------

    """

    tmp = active_selection()
    sel = om.MSelectionList()
    if not is_selection(object):
        sel.add(object.object())
    else:
        sel = object
    activate_selection(sel)
    filename = os.path.join(emplace_directory(path), name)
    cmds.file(filename, force=True, pr=True, es=True, type='OBJexport',
              options="groups=0;ptgroups=0;materials=0;smoothing=0;normals=1")
    activate_selection(tmp)
