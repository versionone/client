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

class GetActionInstances(cskcommands.cmd.CSKCommand):

    Description = 'Get a list of running or previously run Deployment Action Instances.'
    API = 'get_action_instances'
    Examples = '''
_To get all action instances for a given deployment_

    csk-get-action-instances -d "MyApp10"

_To get all action instances for a given service on a deployment_

    csk-get-action-instances -d "MyApp10" -v "Service A"

_To get all action instances for a given service instance on a deployment_

    csk-get-action-instances -d "MyApp10" -i "Service A 1"

_To get all action instances for a specific action on a deployment_

    csk-get-action-instances -d "MyApp10" -a "Clean Logfiles"

_To get all action instances that are Submitted or Processing on a deployment_

    csk-get-action-instances -d "MyApp10" -s "Submitted,Processing"

_To get all action instances on a deployment between two dates_

    csk-get-action-instances -d "MyApp10" --from "1/12/2014" --to "1/19/2014"

_To get all action instances for a given deployment, limited to 10 records_

    csk-get-action-instances -d "MyApp10 -r 10"
'''
    Options = [Param(name='deployment', short_name='d', long_name='deployment',
                     optional=False, ptype='string',
                     doc='Value can be either a Deployment ID or Name.'),
               Param(name='service', short_name='v', long_name='service',
                     optional=True, ptype='string',
                     doc='Value can be either a ServiceID or Name.'),
               Param(name='instance', short_name='i', long_name='instance',
                     optional=True, ptype='string',
                     doc='Value can be either a Service Instance ID or Name.'),
               Param(name='action', short_name='a', long_name='action',
                     optional=True, ptype='string',
                     doc='Value can be either an Action ID or Name.'),
               Param(name='filter', short_name='f', long_name='filter',
                     optional=True, ptype='string',
                     doc='A filter.'),
               Param(name='status', short_name='s', long_name='status',
                     optional=True, ptype='string',
                     doc='A comma separated list of statuses.'),
               Param(name='from', short_name='', long_name='from',
                     optional=True, ptype='string',
                     doc='A "from" date.'),
               Param(name='to', short_name='', long_name='to',
                     optional=True, ptype='string',
                     doc='A "to" date.'),
               Param(name='records', short_name='r', long_name='records',
                     optional=True, ptype='string',
                     doc='Maximum number of records to return.')
               ]

    def main(self):
        results = self.call_api(self.API, ['deployment', 'service', 'instance', 'action', 'filter', 'status', 'from', 'to', 'records'])
        print(results)
