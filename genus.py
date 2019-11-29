def genus(mesh):
    """
    Returns the genus of the input mesh

    Parameters
    ----------
    mesh : MFnMesh
        the input mesh

    Returns
    -------
    int
        the genus of the input mesh
    """

    return mesh.numVertices - mesh.numEdges + mesh.numPolygons - 2
