"""Acquire arguments from the OS and set them as
re-named attributes on an object.

"""

import os


class Aergs(object):
    """
    Acquire arguments from the OS.
    """
    def __init__(self, **kwargs):
        """
        Args: keyword arguments that set an attribute
        with the name of each key to the value found in the OS.

        """
        self._kwargs = kwargs
        self._initialize()

    def _initialize(self):
        for k, v in self._kwargs.iteritems():
            value = os.environ.get(v, '')
            setattr(self, k, value)

    def as_dict(self):
        """
        Return each key and the values found in the OS.

        """
        d = {}
        for k in self._kwargs:
            d[k] = getattr(self, k)
        return d
