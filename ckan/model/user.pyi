"""
This type stub file was generated by pyright.
"""

import datetime
from sqlalchemy import Column, Table, types
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.ext.mutable import MutableDict
from ckan.model import core, domain_object, meta, types as _types

def set_api_key():
    ...

user_table = Table('user', meta.metadata, Column('id', types.UnicodeText, primary_key=True, default=_types.make_uuid), Column('name', types.UnicodeText, nullable=False, unique=True), Column('password', types.UnicodeText), Column('fullname', types.UnicodeText), Column('email', types.UnicodeText), Column('apikey', types.UnicodeText, default=set_api_key), Column('created', types.DateTime, default=datetime.datetime.now), Column('reset_key', types.UnicodeText), Column('about', types.UnicodeText), Column('activity_streams_email_notifications', types.Boolean, default=False), Column('sysadmin', types.Boolean, default=False), Column('state', types.UnicodeText, default=core.State.ACTIVE), Column('image_url', types.UnicodeText), Column('plugin_extras', MutableDict.as_mutable(JSONB)))
class User(core.StatefulObjectMixin, domain_object.DomainObject):
    VALID_NAME = ...
    DOUBLE_SLASH = ...
    @classmethod
    def by_email(cls, email):
        ...
    
    @classmethod
    def get(cls, user_reference):
        ...
    
    @classmethod
    def all(cls):
        '''Return all users in this CKAN instance.

        :rtype: list of ckan.model.user.User objects

        '''
        ...
    
    @property
    def display_name(self):
        ...
    
    @property
    def email_hash(self):
        ...
    
    def get_reference_preferred_for_uri(self):
        '''Returns a reference (e.g. name, id) for this user
        suitable for the user\'s URI.
        When there is a choice, the most preferable one will be
        given, based on readability.
        The result is not escaped (will get done in url_for/redirect_to).
        '''
        ...
    
    def validate_password(self, password):
        '''
        Check the password against existing credentials.

        :param password: the password that was provided by the user to
            try and authenticate. This is the clear text version that we will
            need to match against the hashed one in the database.
        :type password: unicode object.
        :return: Whether the password is valid.
        :rtype: bool
        '''
        ...
    
    password = ...
    @classmethod
    def check_name_valid(cls, name):
        ...
    
    @classmethod
    def check_name_available(cls, name):
        ...
    
    def as_dict(self):
        ...
    
    def number_created_packages(self, include_private_and_draft=...):
        ...
    
    def activate(self):
        ''' Activate the user '''
        ...
    
    def set_pending(self):
        ''' Set the user as pending '''
        ...
    
    def is_deleted(self):
        ...
    
    def is_pending(self):
        ...
    
    def is_in_group(self, group_id):
        ...
    
    def is_in_groups(self, group_ids):
        ''' Given a list of group ids, returns True if this user is in
        any of those groups '''
        ...
    
    def get_group_ids(self, group_type=..., capacity=...):
        ''' Returns a list of group ids that the current user belongs to '''
        ...
    
    def get_groups(self, group_type=..., capacity=...):
        ...
    
    @classmethod
    def search(cls, querystr, sqlalchemy_query=..., user_name=...):
        '''Search name, fullname, email. '''
        ...
    
    @classmethod
    def user_ids_for_name_or_id(cls, user_list=...):
        '''
        This function returns a list of ids from an input that can be a list of
        names or ids
        '''
        ...
    

