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

class ListDocuments(cskcommands.cmd.CSKCommand):

    Description = 'Lists documents in the MongoDB datastore'
    API = 'list_documents'
    Examples = '''
_To list all documents in a specific collection_

    ccl-list-documents -c "workflow_stages"

_To list all documents in a specific collection that have a string match_

    ccl-list-documents -c "workflow_stages" -f "stage 1"
'''
    Options = [Param(name='filter', short_name='f', long_name='filter',
                     optional=True, ptype='string',
                    doc='''A string to use to filter the resulting data. Any row of data that has one field contains the string will be returned.'''),
               Param(name='collection', short_name='c', long_name='collection',
                     optional=True, ptype='string',
                     doc='''A document collection.  "Default" collection will be used if omitted.''')]

    def main(self):
        results = self.call_api(self.API, ['collection', 'filter'])
        print(results)
