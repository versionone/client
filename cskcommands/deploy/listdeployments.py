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

class ListDeployments(cskcommands.cmd.CSKCommand):

    Description = 'Lists all deployed Applications.'
    API = 'list_deployments'
    Examples = '''
_List all non-archived deployments_

    csk-list-deployments

_List all deployments including archived deployments_

    csk-list-deployments -a

_Limit results by name_

    csk-list-deployments -f "My App 4"

_List only deployments in a particular deployment group_

    csk-list-deployments -g "test"

_List deployments created between two dates_

    csk-list-deployments --from "01/16/2014" --to "01/18/2014"
'''
    Options = [Param(name='filter', short_name='f', long_name='filter',
                     optional=True, ptype='string',
                     doc='A filter.'),
               Param(name='hostfilter', short_name='h', long_name='hostfilter',
                     optional=True, ptype='string',
                     doc='Will filter results by the ID, Name or Address of any associated Hosts.'),
               Param(name='groups', short_name='g', long_name='groups',
                     optional=True, ptype='string',
                     doc='A comma separated list of groups.'),
               Param(name='from', short_name='', long_name='from',
                     optional=True, ptype='string',
                     doc='Filter to items created after the "from" date.'),
               Param(name='to', short_name='', long_name='to',
                     optional=True, ptype='string',
                     doc='Filter to items created before the "to" date.'),
               Param(name='show_archived', short_name='a', long_name='show_archived',
                     optional=True, ptype='boolean',
                     doc='Include Archived Deployments in the results.')]

    def main(self):
        results = self.call_api(self.API, ['filter', 'hostfilter', 'groups', 'show_archived', 'from', 'to'])
        print(results)
