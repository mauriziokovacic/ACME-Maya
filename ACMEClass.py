from .hasmethod import *


class ACMEClass(object):
    """
    The base class representation for all the ACME lib classes
    """

    def __init__(self, *args, **kwargs):
        pass

    def __repr__(self):
        return '{}({})'.format(self.__class__.__name__, self.extra_repr() if hasmethod(self, 'extra_repr') else '')
