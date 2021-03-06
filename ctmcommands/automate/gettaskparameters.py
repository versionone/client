#########################################################################
# Copyright 2019 VersionOne
# All Rights Reserved.
# http://www.versionone.com
#########################################################################

import ctmcommands.cmd
from ctmcommands.param import Param


class GetTaskParameters(ctmcommands.cmd.CSKCommand):

    Description = 'Gets a json formatted parameters template for a task.'
    API = 'get_task_parameters'
    Examples = '''
_To get the parameters of a task and redirect to a file_

    ctm-get-task-parameters -t "mytask01" > mytask01_params.json

_To get the parameters of a task_

    ctm-get-task-parameters -t "new example"

_To get the most basic parameter template of a task, minus descriptions and defaults_

    ctm-get-task-parameters -t "new example" -b
'''
    Options = [Param(name='task', short_name='t', long_name='task',
                     optional=False, ptype='string',
                     doc='The ID or Name of a Task.'),
               Param(name='basic', short_name='b', long_name='basic',
                     optional=True, ptype='boolean',
                     doc='Get a basic template with no descriptive details or default values.')]

    def main(self):
        results = self.call_api(self.API, ['task', 'basic'])
        print(results)
