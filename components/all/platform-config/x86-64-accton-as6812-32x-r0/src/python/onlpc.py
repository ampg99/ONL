#!/usr/bin/python
############################################################
# <bsn.cl fy=2013 v=none>
#
#        Copyright 2013, 2014 BigSwitch Networks, Inc.
#
#
#
# </bsn.cl>
############################################################
#
# Platform driver for the Accton AS6812-32x
#
############################################################
import subprocess
import os
from onl.platform.base import *
from onl.vendor.accton import *

class OpenNetworkPlatformImplementation(OpenNetworkPlatformAccton):

    def model(self):
        return "AS6812-32x"

    def platform(self):
        return "x86-64-accton-as6812-32x-r0"

    def _plat_info_dict(self):
        return {
            platinfo.LAG_COMPONENT_MAX : 24,
            platinfo.PORT_COUNT : 32,
            platinfo.ENHANCED_HASHING : True,
            platinfo.SYMMETRIC_HASHING : True,
            }

    def sys_init(self):
        pass

    def sys_oid_platform(self):
        return ".6812.32"

    def baseconfig(self):
        return os.system(os.path.join(self.platform_basedir(), "boot", "x86-64-accton-as6812-32x-r0-devices.sh")) == 0

if __name__ == "__main__":
    print OpenNetworkPlatformImplementation()

