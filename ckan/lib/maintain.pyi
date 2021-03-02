"""
This type stub file was generated by pyright.
"""

import logging

''' This module contains code that helps in maintaining the Ckan codebase. '''
log = logging.getLogger(__name__)
def deprecated(message=...):
    ''' This is a decorator used to mark functions as deprecated.

    It logs a warning when the function is called. If a message is
    passed it is also logged, this can be useful to indicate for example
    that a different function should be used instead.

    Additionally an exception is raised if the functions docstring does
    not contain the word `deprecated`.'''
    ...

def timer(params):
    ''' Decorator function for basic performance testing. It logs the time
    taken to call a function.  It can either be used as a basic decorator or an
    array of parameter names can be passed. If parameter names are passed then
    the logging will include the value of the parameter if it is passed to the
    function. '''
    ...
