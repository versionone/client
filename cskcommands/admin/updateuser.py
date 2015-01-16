#########################################################################
# Copyright 2015 ClearCode Labs
# All Rights Reserved.
# http://www.clearcodelabs.com/license.html
#########################################################################

import cskcommands.cmd
from cskcommands.param import Param

class UpdateUser(cskcommands.cmd.CSKCommand):

    Description = 'Updates a User account.'
    API = 'update_user'
    Examples = '''
    csk-update-user -u "dave.thomas" -s "disabled"  --force
'''
    Options = [Param(name='user', short_name='u', long_name='user',
                     optional=False, ptype='string',
                     doc='The ID or Name of a User account.'),
               Param(name='name', short_name='n', long_name='name',
                     optional=True, ptype='string',
                     doc='The full name of the user.'),
               Param(name='role', short_name='r', long_name='role',
                     optional=True, ptype='string',
                     doc='The users role.  (Valid values: Administrator, Developer, User)',
                     choices=["Administrator", "Developer", "User"]),
               Param(name='email', short_name='e', long_name='email',
                     optional=True, ptype='string',
                     doc='Email address for the user.  Required if "password" is omitted.'),
               Param(name='authtype', short_name='a', long_name='authtype',
                     optional=True, ptype='string',
                     doc='"local" or "ldap".  Default is "local" if omitted.',
                     choices=["local", "ldap"]),
               Param(name='forcechange', short_name='f', long_name='forcechange',
                     optional=True, ptype='integer',
                     doc='Require user to change password. Default is "true" (1) if omitted. (Valid values: 0 or 1).',
                     choices=[0, 1]),
               Param(name='status', short_name='s', long_name='status',
                     optional=True, ptype='string',
                     doc='Status of the new account. Default is "enabled" if omitted. (Valid values: enabled, disabled, locked)',
                     choices=["enabled", "disabled", "locked"]),
               Param(name='expires', short_name='x', long_name='expires',
                     optional=True, ptype='string',
                     doc='Expiration date for this account.  Must be in mm/dd/yyyy format.'),
               Param(name='groups', short_name='g', long_name='groups',
                     optional=True, ptype='string',
                     doc='A list of groups the user belongs to. Group names cannot contain spaces. Comma delimited list.'),
               Param(name='password', short_name='p', long_name='password',
                     optional=True, ptype='string',
                     doc='The new password.'),
               Param(name='generate', long_name='generate',
                     optional=True, ptype='boolean',
                     doc='Generate a new, random password.')]

    def main(self):
        go = False
        if self.force:
            go = True
        else:
            answer = raw_input("Updating a User could affect their ability to log in and use the system.\n\nAre you sure? ")
            if answer:
                if answer.lower() in ['y', 'yes']:
                    go = True

        if go:
            results = self.call_api(self.API, ['user', 'name', 'role', 'email', 'authtype', 'forcechange', 'status', 'expires', 'groups', 'password', 'generate'])
            print(results)
