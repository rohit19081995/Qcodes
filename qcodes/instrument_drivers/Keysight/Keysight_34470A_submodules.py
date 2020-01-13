from .private.Keysight_344xxA_submodules import _Keysight_344xxA


class Keysight_34470A(_Keysight_344xxA):
    """
    This is the qcodes driver for the Keysight 34470A Multimeter
    """
    def __init__(self, name, address, silent=False,
                 **kwargs):
        super().__init__(name, address, silent, **kwargs)
