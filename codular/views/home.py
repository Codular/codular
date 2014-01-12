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
class ViewHome(object):
    def __init__(self, request):
        self.request = request

    @view_config(route_name='home', renderer='home/home.jinja2')
    def home_get(self):
        template_vars = {'menu_active': 'home', 'one': "the one", 'project': 'codular'}
        return template_vars