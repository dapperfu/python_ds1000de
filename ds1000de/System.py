# -*- coding: utf-8 -*-
"""Rigol System Commands Mixin.

SYSTem Commands are the fundamental commands for the operation of an
oscilloscope. They can either be used for operational control or screen data
interception and more.
SYSTem Commands include:
    :RUN
    :STOP
    :AUTO
    :HARDcopy
"""


class System(object):
    """Rigol System commands mixin."""

    def run(self):
        """Start oscilloscope acquiring data."""
        self.w(":RUN")

    def stop(self):
        """Stop oscilloscope from acquiring data."""
        self.w(":STOP")

    def auto(self):
        """Controls the oscilloscope to set the optimum display."""
        self.w(":AUTO")

    def hardcopy(self):
        """Command save a bitmap into the U disc in the form of “HardCopyxxx.bmp”."""
        self.w(":HARDCOPY")
