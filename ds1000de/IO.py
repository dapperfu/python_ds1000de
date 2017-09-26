# -*- coding: utf-8 -*-
"""Low level IO mixin class."""


class IO(object):
    """IO Functions for interacting with the scope."""

    def write(self, cmd):
        """Write a command to the instrument."""
        _, status = self.inst.write(cmd)
        assert(status.value == 0)

    def query(self, cmd):
        """Query the instrument for a value."""
        return self.inst.query(cmd)
