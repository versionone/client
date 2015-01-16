#########################################################################
# Copyright 2015 ClearCode Labs
# All Rights Reserved.
# http://www.clearcodelabs.com/license.html
#########################################################################

import cskcommands.cmd
from cskcommands.param import Param

class DeleteSchedule(cskcommands.cmd.CSKCommand):

    Description = 'Deletes a Task Schedule and all queued execution plans.'
    API = 'delete_schedule'
    Examples = '''
    csk-delete-schedule -s "157545d8-7df9-11e3-ab87-da5f4e6a2990"
'''
    Options = [Param(name='schedule_id', short_name='s', long_name='schedule_id',
                     optional=False, ptype='string',
                     doc='The UUID of the Schedule to delete.')]

    def main(self):
        go = False
        if self.force:
            go = True
        else:
            answer = raw_input("WARNING: This is a utility function.\n\nDeleting a Schedule cannot be undone.\n\nAre you sure? ")
            if answer:
                if answer.lower() in ['y', 'yes']:
                    go = True

        if go:
            results = self.call_api(self.API, ['schedule_id'])
            print(results)
