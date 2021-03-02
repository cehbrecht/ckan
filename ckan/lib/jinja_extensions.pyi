"""
This type stub file was generated by pyright.
"""

import logging
from jinja2 import ext, loaders

log = logging.getLogger(__name__)
def get_jinja_env_options():
    ...

def empty_and_escape(value):
    ''' returns '' for a None value else escapes the content useful for form
    elements. '''
    ...

def regularise_html(html):
    ''' Take badly formatted html with strings etc and make it beautiful
    generally remove surlus whitespace and kill \n this will break <code><pre>
    tags but they should not be being translated '''
    ...

class CkanInternationalizationExtension(ext.InternationalizationExtension):
    ''' Custom translation to allow cleaned up html '''
    def parse(self, parser):
        ...
    


class CkanExtend(ext.Extension):
    ''' Custom {% ckan_extends <template> %} tag that allows templates
    to inherit from the ckan template futher down the template search path
    if no template provided we assume the same template name. '''
    tags = ...
    def __init__(self, environment) -> None:
        ...
    
    def parse(self, parser):
        ...
    


class CkanFileSystemLoader(loaders.FileSystemLoader):
    ''' This is a variant of the jinja2 FileSystemLoader. It allows
    functionality for the ckan_extends tag. When we use the ckan_extends
    tag we only want to look in the ckan/templates directory rather than
    looking thropugh all the template paths. This allows a none base
    template to be able to extend a base ckan template of the same name.
    This functionality allows easy customisation of ckan via template
    inheritance.

    This class is based on jinja2 code which is licensed as follows
======================================================================
    Copyright (c) 2009 by the Jinja Team, see AUTHORS for more details.

Some rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are
met:

    * Redistributions of source code must retain the above copyright
      notice, this list of conditions and the following disclaimer.

    * Redistributions in binary form must reproduce the above
      copyright notice, this list of conditions and the following
      disclaimer in the documentation and/or other materials provided
      with the distribution.

    * The names of the contributors may not be used to endorse or
      promote products derived from this software without specific
      prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
"AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
=====================================================================
    '''
    def get_source(self, environment, template):
        ...
    


class BaseExtension(ext.Extension):
    ''' Base class for creating custom jinja2 tags.
    parse expects a tag of the format
    {% tag_name args, kw %}
    after parsing it will call _call(args, kw) which must be defined. '''
    def parse(self, parser):
        ...
    


class SnippetExtension(BaseExtension):
    ''' Custom snippet tag

    {% snippet <template_name> [, <fallback_template_name>]...
               [, <keyword>=<value>]... %}

    see lib.helpers.snippet() for more details.
    '''
    tags = ...


class UrlForStaticExtension(BaseExtension):
    ''' Custom url_for_static tag for getting a path for static assets.

    {% url_for_static <path> %}

    see lib.helpers.url_for_static() for more details.
    '''
    tags = ...


class UrlForExtension(BaseExtension):
    ''' Custom url_for tag

    {% url_for <params> %}

    see lib.helpers.url_for() for more details.
    '''
    tags = ...


class LinkForExtension(BaseExtension):
    ''' Custom link_for tag

    {% link_for <params> %}

    see lib.helpers.nav_link() for more details.
    '''
    tags = ...


class ResourceExtension(BaseExtension):
    ''' Deprecated. Custom include_resource tag.

    {% resource <resource_name> %}

    see lib.helpers.include_resource() for more details.
    '''
    tags = ...


class AssetExtension(BaseExtension):
    ''' Custom include_asset tag.

    {% asset <bundle_name> %}

    see lib.webassets_tools.include_asset() for more details.
    '''
    tags = ...


def jinja2_getattr(self, obj, attribute):
    """Get an item or attribute of an object but prefer the attribute.
    Unlike :meth:`getitem` the attribute *must* be a bytestring.

    This is a customised version to work with properties
    """
    ...
