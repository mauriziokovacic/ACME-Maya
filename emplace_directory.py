import os


def emplace_directory(path):
    """
    Creates the directory specified by name in the given path if the directory does not exists

    Parameters
    ----------
    path : str
        the path where to create the directory

    Returns
    -------
    str
        return the given path
    """

    if not os.path.exists(path):
        os.makedirs(path)
    return path
