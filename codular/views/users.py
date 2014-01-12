"""
Users view
"""
from pyramid.response import Response
from pyramid.view import ( view_config, view_defaults )

from sqlalchemy.exc import DBAPIError

from ..models import (
    DBSession,
    User,
)

"""
Routes:
'users',       '/users',                   request_method='GET'
'user',        '/users/{id}',              request_method='GET'
'update_user', '/users',                   request_method='POST'
'delete_user', '/users/{id}/delete',       request_method='GET'
'new_user',    '/users/new',               request_method='GET'
'edit_user',   '/users/{id}/edit',         request_method='GET'
"""
class ViewUsers(object):
    def __init__(self, request):
        self.request = request

    @view_config(route_name='users', renderer='json')
    def users(self):
        template_vars = {'menu_active': 'users'}
        return template_vars

    @view_config(route_name='user', renderer='json')
    def user(self):
        template_vars = {'menu_active': 'user'}
        return template_vars

    @view_config(route_name='update_user', renderer='json')
    def update_user(self):
        template_vars = {'menu_active': 'update_user'}
        return template_vars

    @view_config(route_name='delete_user', renderer='json')
    def delete_user(self):
        template_vars = {'menu_active': 'delete_user'}
        return template_vars

    @view_config(route_name='new_user', renderer='users/new.jinja2')
    def new_user(self):
        template_vars = {'menu_active': 'new_user'}
        return template_vars

    @view_config(route_name='edit_user', renderer='json')
    def edit_user(self):
        template_vars = {'menu_active': 'edit_user'}
        return template_vars
