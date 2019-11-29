import maya.api.OpenMaya as om
import maya.api.OpenMayaAnim as oma
import maya.cmds as cmds


def is_mesh(obj):
    return obj.apiType() == om.MFn.kMesh


def get_object(selection):
    return selection.getDependNode(0)


def get_dag_path(selection):
    dag = selection.getDagPath(0)
    dag.extendToShape()
    return dag


def get_mesh(selection):
    dag = get_dag_path(selection)
    return om.MFnMesh(dag)


def get_skin(selection):
    dag = get_dag_path(selection)
    skin = cmds.ls(cmds.listHistory(dag.fullPathName()), type='skinCluster')
    if len(skin) > 0:
        sel = om.MSelectionList()
        sel.add(skin[0])
        obj = get_object(sel)
        return oma.MFnSkinCluster(obj)
    else:
        raise RuntimeError("Selected mesh has no skinCluster")







sel = select_object('beast:Mesh')
dag = get_dag_path(sel)
mesh = get_mesh(sel)
skin = get_skin(sel)
