def linspace(start, end, n, dtype=float):
    """
    Returns a list of n even spaced scalars in range [start, end]

    Parameters
    ----------
    start : int or float
        the starting value
    end : int or float
        the ending value
    n : int
        the number of scalars
    dtype : type (optional)
        the type of the scalars (default is float)

    Returns
    -------
    list
        a list of n scalars in range [start, end]
    """

    r = [i / float(n - 1) for i in list(range(n))]
    return [dtype((1 - t) * start + t * end) for t in r]
