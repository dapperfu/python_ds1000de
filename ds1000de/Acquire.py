# -*- coding: utf-8 -*-
"""Rigol Acquire Commands Sub Module.

ACQuire Commands set the acquire mode for the oscilloscope.
"""


class Acquire(object):
    """ACQuire Commands set the acquire mode for the oscilloscope."""

    def __init__(self, parent):
        """Init acquire subcommands."""
        self.parent = parent

    @property
    def type(self):
        """Current acquire type of the oscilloscope."""
        return self.parent.query(":ACQUIRE:TYPE?")

    @type.setter
    def type(self, value):
        """Setter for acquire type."""
        value = value.upper()
        assert(value in ["NORMAL", "AVERAGE", "PEAKDETECT"])
        self.parent.write(":ACQUIRE:TYPE {}".format(value))

    @property
    def mode(self):
        """Current acquire mode of the oscilloscope."""
        return self.parent.query(":ACQUIRE:MODE?")

    @mode.setter
    def mode(self, value):
        """Setter for acquire type."""
        value = value.upper()
        assert(value in ["RTIME", "ETIME"])
        self.parent.write(":ACQUIRE:MODE {}".format(value))

    @property
    def averages(self):
        """Current average numbers in average mode."""
        return int(self.parent.query(":ACQUIRE:AVERAGES?"))

    @averages.setter
    def averages(self, value):
        """Setter for average acquisition time."""
        assert(value in [2, 4, 8, 16, 32, 64, 128, 256])
        self.parent.write(":ACQUIRE:AVERAGES {}".format(value))
