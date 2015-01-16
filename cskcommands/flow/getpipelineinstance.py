#########################################################################
#
# Copyright 2015 ClearCode Labs
# All Rights Reserved.
# http://www.clearcodelabs.com/license.html
#
#
#########################################################################

import cskcommands.cmd
from cskcommands.param import Param


class GetPipelineInstance(cskcommands.cmd.CSKCommand):

    Description = 'Gets a Pipeline Instance object.'
    API = 'get_pipelineinstance'
    Examples = '''
    csk-get-pipelineinstance -r "Pipeline Instance Name or ID"
'''
    Options = [Param(name='rc', short_name='r', long_name='rc',
                     optional=False, ptype='string',
                     doc='Value can be either a Pipeline Instance ID or Name.'),
               Param(name='include_stages', short_name='s', long_name='include_stages',
                     optional=True, ptype='boolean',
                     doc='If provided, include the Stages, Steps and Plugins - the whole enchilada.')]

    def main(self):
        results = self.call_api(self.API, ['rc', 'include_stages'])
        print(results)
