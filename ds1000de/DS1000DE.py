# -*- coding: utf-8 -*-
"""Python module for Rigol DS1000DE series oscilloscopes."""

import visa


class DS1000DE(object):
    """Python class for Rigol DS1000DE series oscilloscopes."""

    def __init__(self, device="USB"):
        """DS1000DE Init."""
        try:
            rm = visa.ResourceManager()
        except BaseException:
            rm = visa.ResourceManager("@py")
        resources = rm.list_resources()

        resource = [resource for resource in resources if device in resource]
        if len(resource) == 0:
            raise Exception("No devices found matching '{}'".format(device))
        if len(resource) > 1:
            raise Exception(
                "Multiple devices found matching '{}':\n\t{}".format(
                    device, "\n\t".join(resource)))

        self.resource = resource[0]

        self.inst = rm.open_resource(self.resource)
        self.r = self.inst.query
        self.w = self.inst.write

    @property
    def idn(self):
        """Return *IDN?."""
        return self.r("*IDN?")

    @property
    def manufacturer(self):
        """Return manufacturer."""
        manufacturer, model, serial, software = self.idn.split(",")
        return manufacturer

    @property
    def model(self):
        """Return model."""
        manufacturer, model, serial, software = self.idn.split(",")
        return model

    @property
    def serial(self):
        """Return serial."""
        manufacturer, model, serial, software = self.idn.split(",")
        return serial

    @property
    def software(self):
        """Return software version."""
        manufacturer, model, serial, software = self.idn.split(",")
        return software
