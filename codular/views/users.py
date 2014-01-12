"""
Users view
"""
from pyramid.response import Response
from pyramid.view import ( view_config, view_defaults )
from pyramid.security import authenticated_userid
from pyramid.httpexceptions import HTTPFound

from deform import Form
from deform.exception import ValidationFailure
from ..forms import Registration

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

    @view_config(route_name='update_user', request_method='POST', renderer='users/new.jinja2')
    def update_user(self):
        template_vars = {'menu_active': 'update_user'}
        form = Form(Registration().bind(request=self.request), buttons=('submit',),
                action=self.request.route_url('update_user'))
        if 'submit' in self.request.POST: # detect that the submit button was clicked

            controls = self.request.POST.items() # get the form controls

            try:
                form_data = form.validate(controls)  # call validate
            except ValidationFailure as e: # catch the exception
                template_vars['form'] = form.render() # re-render the form with an exception
                return template_vars

            # if user is logged, we update his profile. Else we create a new user.
            userid = authenticated_userid(self.request)
            if userid:
                user =  User.by_id(userid)
                # WARNING: only update authorized values

            else:
                del(form_data['csrf'])
                user = User(**form_data)
                DBSession.add(user)

            url = self.request.route_url('home')
            return HTTPFound(location=url)
        template_vars['form'] = form.render()
        return template_vars

    @view_config(route_name='delete_user', renderer='json')
    def delete_user(self):
        template_vars = {'menu_active': 'delete_user'}
        return template_vars

    @view_config(route_name='new_user', renderer='users/new.jinja2')
    @view_config(route_name='register', renderer='users/new.jinja2')
    def new_user(self):
        template_vars = {'menu_active': 'new_user'}
        form = Form(Registration().bind(request=self.request), buttons=('submit',),
                action=self.request.route_url('update_user'))
        template_vars['form'] = form.render()
        return template_vars

    @view_config(route_name='edit_user', renderer='json')
    def edit_user(self):
        template_vars = {'menu_active': 'edit_user'}
        return template_vars
