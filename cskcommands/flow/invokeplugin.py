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


class InvokePlugin(cskcommands.cmd.CSKCommand):

    Description = """Execute a specified Flow Plugin Function

Response varies based on the specified Plugin."""

    API = 'invoke_plugin'
    Examples = ''''''
    Options = [Param(name='plugin', short_name='p', long_name='plugin',
                     optional=False, ptype='string',
                     doc='Plugin.Module containing the desired function to invoke. (ex: github.main)'),
               Param(name='method', short_name='m', long_name='method',
                     optional=False, ptype='string',
                     doc='Method to invoke. (ex "get_issue")'),
               Param(name='args', short_name='a', long_name='args',
                     optional=True, ptype='string',
                     doc='A JSON object containing Plugin Function specific arguments.')
               ]

    def main(self):
        results = self.call_api(self.API, ['plugin', 'method', 'args'])
        print(results)