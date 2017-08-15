# -*- coding: utf-8 -*-
import visa

class DS1000DE(object):
    def __init__(self, device="USB0"):
        rm = visa.ResourceManager()
        resources = rm.list_resources()
        
        resource = [resource for resource in resources if device in resource]
        if len(resource) == 0:
            raise Exception("No devices found matching '{}'".format(device))
        if len(resource) > 1:
            raise Exception("Multiple devices found matching '{}':\n\t{}".format(device, "\n\t".join(resource)))
        
        self.resource = resource[0]
        
        self.scope = rm.open_resource(resource[0])