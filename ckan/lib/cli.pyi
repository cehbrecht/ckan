"""
This type stub file was generated by pyright.
"""

import click
import ckan.lib.maintain as maintain

_cli_test_request_context = None
@maintain.deprecated('Use @maintain.deprecated instead')
def deprecation_warning(message=...):
    '''
    DEPRECATED

    Print a deprecation warning to STDERR.

    If ``message`` is given it is also printed to STDERR.
    '''
    ...

@maintain.deprecated()
def error(msg):
    '''
    DEPRECATED

    Print an error message to STDOUT and exit with return code 1.
    '''
    ...

@maintain.deprecated('Instead you can probably use click.confirm()')
def query_yes_no(question, default=...):
    """DEPRECATED

    Ask a yes/no question via input() and return their answer.

    "question" is a string that is presented to the user.
    "default" is the presumed answer if the user just hits <Enter>.
        It must be "yes" (the default), "no" or None (meaning
        an answer is required of the user).

    The "answer" return value is one of "yes" or "no".
    """
    ...

class MockTranslator(object):
    def gettext(self, value):
        ...
    
    def ugettext(self, value):
        ...
    
    def ungettext(self, singular, plural, n):
        ...
    


def load_config(config, load_site_user=...):
    ...

@maintain.deprecated('Instead use ckan.cli.cli.CkanCommand or extensions ' 'should use IClick')
def paster_click_group(summary):
    '''DEPRECATED

    Return a paster command click.Group for paster subcommands

    :param command: the paster command linked to this function from
        setup.py, used in help text (e.g. "datastore")
    :param summary: summary text used in paster's help/command listings
        (e.g. "Perform commands to set up the datastore")
    '''
    class PasterClickGroup(click.Group):
        '''A click.Group that may be called like a paster command'''
        ...
    
    

click_config_option = click.option('-c', '--config', default=None, metavar='CONFIG', help=u'Config file to use (default: development.ini)')
class CkanCommand(paste.script.command.Command):
    '''DEPRECATED - Instead use ckan.cli.cli.CkanCommand or extensions
    should use IClick.

    Base class for classes that implement CKAN paster commands to
    inherit.'''
    parser = ...
    default_verbosity = ...
    group_name = ...

