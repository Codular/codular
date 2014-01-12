"""
User view
"""
from pyramid.response import Response
from pyramid.view import view_config
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
Is : User edit action
Route : /users
"""
@view_config(route_name='update_user', request_method='POST', renderer='users/new.jinja2')
def update_user(request):
    form = Form(Registration().bind(request=request), buttons=('submit',),
            action=request.route_url('update_user'))
    if 'submit' in request.POST: # detect that the submit button was clicked

        controls = request.POST.items() # get the form controls

        try:
            form_data = form.validate(controls)  # call validate
        except ValidationFailure as e: # catch the exception
            return {'form':form.render()} # re-render the form with an exception

        # if user is logged, we update his profile. Else we create a new user.
        userid = authenticated_userid(request)
        if userid:
            user =  User.by_id(userid)

        else:
            del(form_data['csrf'])
            user = User(**form_data)
            DBSession.add(user)

        url = request.route_url('home')
        return HTTPFound(location=url)
    return {'form': form.render()}

"""
Is : Registration form
Route : /users/new
"""
@view_config(route_name='new_user', renderer='users/new.jinja2')
@view_config(route_name='register', renderer='users/new.jinja2')
def new_users(request):
    form = Form(Registration().bind(request=request), buttons=('submit',),
            action=request.route_url('update_user'))
    return {'form': form.render()}

