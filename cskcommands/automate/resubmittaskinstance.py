#########################################################################
# Copyright 2015 ClearCode Labs
# All Rights Reserved.
# http://www.clearcodelabs.com/license.html
#########################################################################

import cskcommands.cmd
from cskcommands.param import Param

class ResubmitTaskInstance(cskcommands.cmd.CSKCommand):

    Description = 'Resubmit an Errored or Cancelled Task Instance, for another attempt at completion.  Only valid on Instances that ended with Error or were Cancelled.'
    API = 'resubmit_task_instance'
    Examples = '''
    ccl-resubmit-task-instance -i 43667
'''
    Options = [Param(name='instance', short_name='i', long_name='instance',
                     optional=False, ptype='string',
                     doc='The Task Instance number.')]

    def main(self):
        results = self.call_api(self.API, ['instance'])
        print(results)
