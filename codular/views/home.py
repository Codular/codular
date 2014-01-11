"""
Home view
"""
from pyramid.response import Response
from pyramid.view import view_config

from sqlalchemy.exc import DBAPIError

from ..models import (
    DBSession,
    User,
)

"""
Is : Homepage
Route : /
"""
@view_config(route_name='home', renderer='home/home.jinja2')
def view_home(request):
    return {'one': "the one", 'project': 'codular'}