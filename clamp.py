def clamp(value, lower, upper):
    """
    Clamps a given value in the range [lower, upper]

    Parameters
    ----------
    value : int or float
        the value to clamp
    lower : int or float
        the lower bound
    upper : int or float
        the upper bound

    Returns
    -------
    int or float
        the clamped value
    """

    return max(lower, min(upper, value))
